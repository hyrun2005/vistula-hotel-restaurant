from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def mainPage(request):
    return render(request, 'main_page.html', {})