from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Mall
# Create your views here.

def mall(request):
    mall = Mall.objects.all()
    return render(request, 'home/mall.html',{'malls':mall})