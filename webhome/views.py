from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'webhome/content.html')
def login(request):
    return render(request, 'webhome/login.html')
