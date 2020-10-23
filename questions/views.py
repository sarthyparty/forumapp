from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import Question, Answer
from django.db.models import Q



# Create your views here.

def home(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/search/' + request.POST['keyword'] + '/')

    else:
        form = SearchForm()
    return render(request, 'home.html', {'form': form})


def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions': questions})


def ask_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = Question(question=str.capitalize(request.POST['question']))
            new_question.save()
            return HttpResponseRedirect('/')
    else:
        form = QuestionForm()

    return render(request, 'ask_question.html', {'form': form})


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})


def new_answer(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            new_answer = Answer(answer=str.capitalize(request.POST['answer']),
                                first_name=str.capitalize(request.POST['first_name']),
                                last_name=str.capitalize(request.POST['last_name']),
                                question=question)
            new_answer.save()
            return HttpResponseRedirect('/q/' + id)
    else:
        form = AnswerForm()

    return render(request, 'new_answer.html', {'form': form, 'question': question})

def search(request, keyword):
    questions = list(Question.objects.filter(question__icontains=keyword))
    answers = Answer.objects.filter(answer__icontains=keyword)
    for answer in answers:
        if answer.question not in questions:
            questions.append(answer.question)
    return render(request, 'questions.html', {'questions': questions})
