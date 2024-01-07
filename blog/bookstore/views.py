from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Home Page') 
def users(request):
    return HttpResponse('users Page') 
def about(request):
    return HttpResponse('about Page') 