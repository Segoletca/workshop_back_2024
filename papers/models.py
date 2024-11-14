from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


# class Likes(models.Model):
#     user = models.ForeignKey(Author, on_delete=models.DO_NOTHING)


class Paper(models.Model):
    '''
    Описание модели статей
    '''
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default='None')
    content = models.TextField()
    # likes = models.ForeignKey(Likes, on_delete=models.DO_NOTHING, default=0)
