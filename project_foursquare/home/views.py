from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Park,Mall
from .forms import PostForm

# Create your views here.
# def park(request):
#     isi=Park.objects.all()
#     return render(request, 'home/new_form.html',{'isi':isi})

def park_detail(request, park_id):
    park = Park.objects.get(pk=park_id)
    return render(request, 'home/park_detail.html', {'data':park})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            return redirect('input_post')
    else:
        form = PostForm()
    isi=Park.objects.all()
    return render(request, 'home/new_form.html', {'form':form,'isi':isi})

def mall(request):
    mall = Mall.objects.all()
    return render(request, 'home/mall.html',{'malls':mall})

def mall_detail(request, mall_id):
    malls = Mall.objects.get(pk=mall_id)
    return render(request, 'home/mall_detail.html', {'data':malls})

def form(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('form')
    else:
        form = PostForm()
    mall = Mall.objects.all()
    return render(request,'home/input_mall.html', {'form': form,'malls':mall})