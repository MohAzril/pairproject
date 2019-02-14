from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('park/<int:park_id>', views.park_detail, name='park_detail'),
    path('mall/<int:mall_id>', views.mall_detail, name='mall_detail'),
    path('mall', views.mall, name='mall'),
    path('', views.form, name='malls'),
    path('park', views.input_post, name='parks'),
]
