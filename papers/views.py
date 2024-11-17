from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Papers, Category
from .serializers import PapersSerializer


# Create your views here.
class PaperListAPIView(ListAPIView):
    queryset = Papers.objects.all().order_by('-time_create')
    serializer_class = PapersSerializer


# class PaperUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Papers.objects.all().order_by('-time_create')
#     serializer_class = PapersSerializer
#
#
# class TopicListAPIView(APIView):
#     def get(self, request, category=None):
#         try:
#             category = Category.objects.get(id=category)
#             papers = Papers.objects.filter(category=category)
#             serializer = PapersSerializer(papers, many=True)
#             return Response(serializer.data)
#         except ObjectDoesNotExist:
#             return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
