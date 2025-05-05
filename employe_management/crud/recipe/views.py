from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def home(request):
    objects=Recipe.objects.all()
    return render(request,'list.html',{'employees':objects})

