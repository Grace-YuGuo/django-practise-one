from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
def about_me(request):
    return HttpResponse("This is rendered by about app view.py file first funciton of about")