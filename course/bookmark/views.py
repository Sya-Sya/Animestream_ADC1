from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bookmark(request):
    context={
        'Welcome_text':"Welcome to Bookmark"
    }
    return render(request, 'bookmark.html', context)

def home(request):
    context={
        'Welcome_text':"Welcome to Home"
    }
    return render(request, 'home.html', context)

def login(request):
    context={
        'Welcome_text':"Welcome to your profile"
    }
    return render(request, 'login.html', context)
