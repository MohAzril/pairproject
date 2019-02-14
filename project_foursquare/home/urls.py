from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('park', views.home, name='park'),
    path('park/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('mall/<int:mall_id>', views.mall_detail, name='mall_detail'),
    path('mall', views.mall, name='mall'),
    path('', views.form, name='form'),
]