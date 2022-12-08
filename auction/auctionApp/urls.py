from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getUsersQuestions/<int:user_id>/', views.getUserQuestions, name='questions'),
]