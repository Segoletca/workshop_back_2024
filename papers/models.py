from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Papers(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE,
                               null=True)
    content = models.TextField(max_length=2500)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
