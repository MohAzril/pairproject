from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils import timezone
from .models import Park,Mall

# Create your views here.
def home(request):
    isi=Park.objects.all()
    return render(request, 'home/park.html',{'isi':isi})

def blog_detail(request, blog_id):
    blogging = Park.objects.get(pk=blog_id)
    return render(request, 'home/park_detail.html', {'data':blogging})

def mall(request):
    mall = Mall.objects.all()
    return render(request, 'home/mall.html',{'malls':mall})

