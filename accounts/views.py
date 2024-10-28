from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from .forms import RegisterForm  # Ensure this matches your actual form name
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def registration(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after registration
            messages.success(request, 'Account created successfully')
            return redirect('main_page')  # Redirect as needed

    context = {'form': form}
    return render(request, 'register_user.html', context)

@csrf_exempt
def login_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Adjust this if using phone_number
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('main_page')
        else:
            messages.info(request, 'Username or Password is incorrect')

    template = 'login_user.html'
    context = {}
    return render(request, template, context)

@csrf_exempt
def logoutUser(request):
    logout(request)
    return redirect('login_in')
