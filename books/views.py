'''
Файл для представлений, то есть классов или функций, в которых мы прописываем то,
как будет обрабатываться запрос, который мы описываем тем или иным классом (функцией)
'''
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class AuthorAPIView(APIView):
    '''
    Класс, в котором все операции над нашими данными пишутся вручную
    тут можно писать несколько методов (post, get, put, patch, delete)
    '''
    def post(self, requests, *args, **kwargs):
        serializer = AuthorSerializer(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BookCreateAPIView(CreateAPIView):
    '''
    Класс представления для создания новой книги в базе данных  
    '''
    serializer_class = BookSerializer
    

class BookListAPIView(ListAPIView):
    '''
    Класс представления для просмотра всех книг а базе данных
    '''
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorViewSet(ModelViewSet):
    '''
    Вьюсет для автора
    Вьюсеты создают все http методы по умолчанию
    Но иногда это может быть неудобно, а почему - вопрос на подумать
    '''
    queryset = Author.objects.all()
    serializer_class = AuthorViewSetSerializer


from rest_framework.response import Response

