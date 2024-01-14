from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.published.all() 
    return render(request,'main.html')
