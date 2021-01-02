from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *


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

                Phone_num=Phone.objects.create(phone_num=phone_num,New=user)
                Phone_num.save()
                messages.info(request, 'Registration Successfully')
                return redirect('/')
                print('user created')
        else:
            messages.info(request, 'Password Already Taken')
            return render(request, 'webhome/register.html')
    else:
        return render(request, 'webhome/register.html')
