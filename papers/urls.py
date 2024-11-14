from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
# router.register(r'test_papers', PapersAPIView)

urlpatterns = [
    # path('hello/', PapersAPIView.as_view()),
    path('', include(router.urls)),
    # path('profile/<slug:user>/', ProfileAPIView.as_view()),
    path('getUsers/', UserAPIView.as_view()),
    path('whoami/', ProfileAPIView.as_view()),
    path('list/', PaperListAPIView.as_view()),
]
