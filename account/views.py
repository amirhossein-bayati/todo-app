from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


def homePage(request):
    return render(request, 'account/home-page.html')

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:home')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)

def loginPage(request):
    if request.method == "POST":
        cd = request.POST
        username = cd['username']
        password = cd["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('account:home')
            else:
                messages.error(request, "User is not active")
        else:
            messages.error(request, "Username Or password is Incorrect")

    return render(request, 'account/login.html')