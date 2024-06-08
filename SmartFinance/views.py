from django.shortcuts import render,HttpResponse,redirect
from .models import Author,category,product,userregister
# Create your views here.
def first(request):
    return HttpResponse("This is Love website.")

