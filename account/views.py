from django.shortcuts import render, redirect
from django.http import HttpResponse
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