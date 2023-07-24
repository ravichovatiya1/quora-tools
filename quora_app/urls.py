from django.urls import path
from . import views

# app name
app_name = "quora_app"


# base pattern define
index_patterns = [
    path('', views.index, name="index"),
]

# questions pattern
questions_patterns = [
    path('post/view/',views.post_questions_view, name="post_questions_view"),
    path('post/create/',views.post_questions_create, name="post_questions_create"),
    path('post/update/<uuid:question_id>/',views.post_questions_update, name="post_questions_update"),
    path('post/delete/<uuid:question_id>/',views.post_questions_delete, name="post_questions_delete"),
]


# Answer patters
answers_patterns =[
    path('add/', views.answer_add, name="answer_add"),
    path('like/', views.like_answer, name="like"),
]

