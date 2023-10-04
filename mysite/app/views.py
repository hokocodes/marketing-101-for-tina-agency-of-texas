from django.shortcuts import render, redirect
from django.contrib.auth import logout
from datetime import datetime

from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)