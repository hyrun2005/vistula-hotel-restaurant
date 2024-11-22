from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from .models import Category


# Create your views here.
def mainPageRes(request):
    return render(request, 'main_page_res.html', {})


def menu(request):
    # Fetch all categories along with their related dishes
    categories = Category.objects.prefetch_related('dishes').all()

    return render(request, 'menu_page.html', {'categories': categories})

