
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('park', views.park, name='park'),
    path('park/<int:park_id>', views.park_detail, name='park_detail'),
    path('park', views.input_post, name="input_post"),
    path('', views.mall, name='mall'),
]