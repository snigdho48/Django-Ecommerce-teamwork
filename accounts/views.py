from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .models import *


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


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone_num = request.POST['phone']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return render(request, 'webhome/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return render(request, 'webhome/register.html')
            elif Phone.objects.filter(phone_num=phone_num).exists():
                messages.info(request, 'phoneNumber already taken')
                return render(request, 'webhome/register.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)

                user.save()

                Phone_num = Phone.objects.create(phone_num=phone_num, New=user)
                Phone_num.save()
                messages.info(request, 'Registration Successfully')
                return redirect('login')
                print('user created')
        else:
            messages.info(request, 'Password Already Taken')
            return render(request, 'webhome/register.html')
    else:
        return render(request, 'webhome/register.html')
