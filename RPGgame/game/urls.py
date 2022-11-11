
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="home"),
    path('register/', views.RegisterView.as_view(), name="register")
]
