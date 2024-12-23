from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Papers, Category
from .permissions import IsOwnerOrReadOnly
from .serializers import PapersSerializer, CreatePaperSerializer


class PaperListAPIView(ListAPIView):
    queryset = Papers.objects.all().order_by('-time_create')
    serializer_class = PapersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PaperCreateAPIView(CreateAPIView):
    queryset = Papers.objects.all()
    serializer_class = CreatePaperSerializer
    permission_classes = (IsAuthenticated,)


class PaperUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Papers.objects.all().order_by('-time_create')
    serializer_class = PapersSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class FilterListAPIView(APIView):
    def get(self, request, category=None, author=None):
        try:
            if category:
                category = Category.objects.get(id=category)
                papers = Papers.objects.filter(category=category).order_by('-time_create')
            if author:
                author = User.objects.get(id=author)
                papers = Papers.objects.filter(author=author).order_by('-time_create')

            serializer = PapersSerializer(papers, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
