from django import forms
from django.core import validators
from .constants import *


class QuestionForm(forms.Form):
    question = forms.CharField(label='', max_length=question_max, required=False, widget=forms.Textarea)


class AnswerForm(forms.Form):
    answer = forms.CharField(label='', max_length=answer_max, required=False,
                             widget=forms.Textarea)
    first_name = forms.CharField(label='First Name', max_length=20, validators=[
        validators.RegexValidator(regex='^[a-zA-Z\s]*$', message="Only letters allowed!")])
    last_name = forms.CharField(label='Last Name', max_length=20, validators=[
        validators.RegexValidator(regex='^[a-zA-Z\s]*$', message="Only letters allowed!")])


class SearchForm(forms.Form):
    keyword = forms.CharField(label='Search', max_length=20)
