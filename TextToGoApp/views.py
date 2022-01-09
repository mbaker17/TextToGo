from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView

# Create your views here.
from .forms import CreateUserForm, OrderObjectForm

def index(request):
    return render(request, 'pages/index.html')

def schedule(request):
    return render(request, 'pages/schedule.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        context = {}

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
                return render(request, 'pages/login.html', context)

        return render(request, 'pages/login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'pages/register.html', context)

def createOrderObject(request):
    form = OrderObjectForm()
    if request.method == 'POST':
        form = OrderObjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}

    return render(request, 'pages/createOrder.html', context)