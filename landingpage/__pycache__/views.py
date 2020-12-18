from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import *

# Create your views here.
def index(request):
    Blogs = Blog.objects.all()
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request,"Query Sent Successfully")
        return redirect('index')
    else:
        return render(request,'index.html', {'Blogs': Blogs})
        
def blogdetail(request, bid):
    blog = Blog.objects.get(id=bid)
    return render(request, 'blog_detail.html', {'Blog': blog})
