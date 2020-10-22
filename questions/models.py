from django.db import models
from .constants import *
# Create your models here.

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=question_max)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    answer = models.CharField(max_length=answer_max)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

