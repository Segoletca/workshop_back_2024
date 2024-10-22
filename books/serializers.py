'''
Файл для описания сериализаторов для наших представлений. Сериализаторы - 
это классы, в которых описывается то, как превращать данные в JSON и обратно
'''
from rest_framework import serializers

from .models import *


class AuthorSerializer(serializers.Serializer):
    '''
    Более низкоуровневый вариант создания сериализаторов
    Здесь мы почти все пишем вручную
    '''
    name = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class BookSerializer(serializers.ModelSerializer):
    '''
    Сериализатор на основе модели Book
    Сериализаторы нужны для обработки данных и превращения их из JSON в объекты python
    '''
    author = AuthorSerializer() #Делаем поле автора из нашего сериализатора авторов
    
    class Meta:
        model = Book
        exclude = ('id', ) # exclude исключает все поля, которые есть внури кортежа
        
    def create(self, validated_data):
        '''
        Прописываем вручную более приемлимое создание автора
        '''
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book


class AuthorViewSetSerializer(serializers.ModelSerializer):
    '''
    Другой вариант написания сериализатора для модели автора
    '''
    class Meta:
        model = Author
        fields = ['id', 'name']
