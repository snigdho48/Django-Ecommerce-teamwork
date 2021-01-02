from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.views import PasswordResetView


# Create your views here.
def index(request):
    return render(request, 'webhome/content.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('username')
        password = request.POST.get('password')
        User._meta.get_field('email')._unique = True

        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=password)

        elif User.objects.filter(email=email).exists():
            username = User.objects.get(email=email.lower()).username
            user = authenticate(username=username, password=password)

        else:
            messages.info(request, 'Enter valid username or email')
            return render(request, 'webhome/login.html')

        if user is not None:

            auth.login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'incorrect password.')

            return render(request, 'webhome/login.html')

    else:
        return render(request, 'webhome/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
