from django.urls import path
from .views import *

urlpatterns = [
    # path('profile/'),  # Посмотреть список своих статей
    path('general/', PaperListAPIView.as_view()),  # Посмотреть список всех статей начиная с самой свежей
    path('detail/<int:pk>', PaperUpdateAPIView.as_view()),  # Посмотреть/изменить конкретную статью подробно
    # path('topic/<int:category>', TopicListAPIView.as_view())  # Отфильтровать статьи по категориям
]
