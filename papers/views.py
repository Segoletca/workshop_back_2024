from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Papers, Category
from .serializers import PapersSerializer


class PaperListAPIView(ListAPIView):
    queryset = Papers.objects.all().order_by('-time_create')
    serializer_class = PapersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


# class PaperCreateAPIView()

class PaperUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Papers.objects.all().order_by('-time_create')
    serializer_class = PapersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TopicListAPIView(APIView):
    def get(self, request, category=None):
        try:
            category = Category.objects.get(id=category)
            papers = Papers.objects.filter(category=category)
            serializer = PapersSerializer(papers, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
