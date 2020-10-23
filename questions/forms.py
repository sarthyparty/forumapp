from django import forms
from django.core import validators
from .constants import *


class QuestionForm(forms.Form):
    question = forms.CharField(label='Question', max_length=question_max, required=False, widget=forms.Textarea)


class AnswerForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=20, validators=[
        validators.RegexValidator(regex='^[a-zA-Z\s]*$', message="Only letters allowed!")])
    last_name = forms.CharField(label='Last Name', max_length=20, validators=[
        validators.RegexValidator(regex='^[a-zA-Z\s]*$', message="Only letters allowed!")])
    answer = forms.CharField(label='Answer', max_length=answer_max, required=False,
                             widget=forms.Textarea)


class SearchForm(forms.Form):
    keyword = forms.CharField(label='Search', max_length=20)
