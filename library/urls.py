"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .spectacular import urlpatterns as spectacular


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls'))
] + spectacular


'''
Файл urls.py в Django отвечает за маршрутизацию, определяя, 
какие URL-адреса в проекте будут обрабатываться определёнными представлениями (views). 

urlpatterns: Это список, который содержит маршруты (URL-шаблоны) и указывает, 
какое представление (view) должно быть вызвано при обращении к каждому из этих маршрутов.

Этот файл - основной в проекте и, чтобы его не засорять, мы создаем в каждом приложении
свой файл с именём urls.py. Чтобы джанго увидел его, нужно описать его здесь функцией include
'''