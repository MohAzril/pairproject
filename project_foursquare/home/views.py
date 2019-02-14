from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Park,Mall

# Create your views here.

def home(request):
    isi=Mall.objects.all()
    return render(request, 'home/content.html',{'isi':isi})

