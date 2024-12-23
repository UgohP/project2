from django.shortcuts import render
from email.mime import application
from itertools import product
import random
from ssl import create_default_context
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from .filters import *
from django.contrib.auth.decorators import login_required
from bluemartin.decorators import *
from django.views.generic import ListView
from django.views.generic.edit import *
from users.models import *

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def myBlog(request):
    vendor = request.user.vendor
    blog = Blog.objects.filter(posted_by=vendor) 

    context = {'blog':blog}
    return render(request, 'my_blog.html', context)

@login_required(login_url='login')
def blogs(request):
    blog = Blog.objects.all()
    vendor = Vendor.objects.all()
    context = {'blog':blog, 'vendor': vendor,}
    return render(request, 'blog.html', context)

@login_required(login_url='login')
def getBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog':blog}
    return render(request, 'get_blog.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def createBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.posted_by = request.user.vendor

            blog.save()
        messages.success(request, str(blog.business_name) + ', your blog has been posted Successfully!!')
        return redirect('my_blog')
    else:
        form = BlogForm()
    

    context = {'form':form}
    return render(request, 'createBlog.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!!')
            return redirect('my_blog')
    context = {'form':form}
    return render(request, 'update_blog.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def deleteBlog(request, pk):

    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Deleated Successfully!!')
        return redirect('my_blog')
    context = {'blog': blog}
    return render(request, 'delete_blog.html', context)
