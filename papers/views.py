from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from books.models import Book
from books.serializers import BookSerializer
from django.contrib.auth.models import User
from .serializers import UserViewSetSerializer

# Create your views here.

# class PapersAPIView(ListAPIView):
#     queryset =

def test_request(request):
    return HttpResponse("Приложение papers!!!")


class PapersAPIView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserViewSetSerializer
    print(User.objects.all())

# class DeleteLedgerCategory(DestroyAPIView):
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         queryset = Category.objects.filter(company = self.request.user.currently_activated_company, id=self.kwargs['pk'])
#         return queryset
#
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if instance.is_default == True:
#             return Response("Cannot delete default system category", status=status.HTTP_400_BAD_REQUEST)
#         self.perform_destroy(instance)
