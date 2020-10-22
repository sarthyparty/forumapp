from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questions', views.questions, name='questions'),
    path('ask_question', views.ask_question, name='ask_question'),
    path('<id>', views.question_detail, name='question_detail'),
    path('new_answer/<id>/', views.new_answer, name='new_answer')
]
