from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Park,Mall

# Create your views here.

def home(request):
    isi=Park.objects.all()
    return render(request, 'home/park.html',{'isi':isi})

def blog_detail(request, blog_id):
    blogging = Park.objects.get(pk=blog_id)
    return render(request, 'home/park_detail.html', {'data':blogging})