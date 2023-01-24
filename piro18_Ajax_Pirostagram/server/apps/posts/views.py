from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def post(request):
    return render(request, 'post.html')