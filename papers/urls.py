from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:author>', FilterListAPIView.as_view()),  # Посмотреть список своих статей или других пользователей
    path('general/', PaperListAPIView.as_view()),  # Посмотреть список всех статей начиная с самой свежей
    path('create/', PaperCreateAPIView.as_view()),  # Создать статью
    path('detail/<int:pk>', PaperUpdateAPIView.as_view()),  # Посмотреть/изменить конкретную статью (изменять может только владелец)
    path('topic/<int:category>', FilterListAPIView.as_view()),  # Отфильтровать статьи по категориям
]
