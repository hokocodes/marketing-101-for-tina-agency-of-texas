from django.shortcuts import render, redirect
from django.contrib.auth import logout
from datetime import datetime

from django.http import HttpResponse
# Create your views here.



def home(request):
    return HttpResponse('home.html')

def logout_view(request):
    logout(request)
    return redirect('/')