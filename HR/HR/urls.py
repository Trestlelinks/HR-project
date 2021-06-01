"""HR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path
from Login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('login', views.handlelogin, name='handlelogin'),
    path('dash', views.dash1, name='dash'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('candidate',views.reg,name='reg'),
    path('index',views.indx,name='index'),
    path('success',views.succs,name='success'),
    path('candidatelogin',views.candidatelogin,name='candidatelogin'),
    path('loginsuccess', views.loginsuccess,name='loginsuccess'),
]
