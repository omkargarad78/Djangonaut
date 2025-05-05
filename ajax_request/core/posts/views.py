from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages



def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})

from django.shortcuts import redirect

def like_post(request):
    if request.method == 'POST':
        post_id = request.GET.get('post_id')
        likedpost = Post.objects.get(pk=post_id)
        m = Likes(post=likedpost)
        m.save()
        messages.success(request, "You liked this post!")
        return redirect('home')  # Redirect back to the homepage
    else:
        messages.error(request, "Invalid request method!")
        return redirect('home')

