from django.shortcuts import render
from django.http import HttpResponse


def homePage(request):
    return render(request, 'account/home-page.html')