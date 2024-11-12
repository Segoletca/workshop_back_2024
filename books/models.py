'''
Файл для описания моделей нашего приложения.
Модели - это классы, которые описывают таблицы в базе данных.
'''
from django.db import models


class Book(models.Model):
    '''
    Описание модели книг, то есть представление таблицы из базы данных в Python
    '''
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    

class Author(models.Model):
    '''
    Описание модели книг, то есть представление таблицы из базы данных в Python
    '''
    name = models.CharField(max_length=100)
