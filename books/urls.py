from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'authors', AuthorViewSet)


urlpatterns = [
    path('create/book/', BookCreateAPIView.as_view()),
    path('list/book/', BookListAPIView.as_view()),
    path('create/author/', AuthorAPIView.as_view()),
    path('', include(router.urls)),
]

'''
Пути нашего приложения books
'''