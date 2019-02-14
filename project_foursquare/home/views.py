from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home/content.html',{})