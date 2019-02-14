from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.
ender(request, 'home/base.html')
=======
def home(request):
    return render(request, 'home/content.html',{})

