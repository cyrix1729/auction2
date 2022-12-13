from django.urls import path
from . import views
from .views import user_api, listings_api

urlpatterns = [
    path('', views.index, name='index'),
    path('api/listings/', listings_api, name="listings api"),
    path('getUsersQuestions/<int:user_id>/', views.getUserQuestions, name='questions'),
    path('api/user', user_api),
]