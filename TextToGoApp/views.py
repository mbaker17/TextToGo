from sqlite3 import Date
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView

# Create your views here.
from .models import OrderObject
from .forms import CreateUserForm, OrderObjectForm, OrderObjectEditForm, OrderObjectEditFormDate, newForm

from datetime import date, timedelta

def index(request):
    return render(request, 'pages/index.html')

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

def selectDate(request):

    one = date.today()
    two = one + timedelta(days=1)
    three = one + timedelta(days=2)
    four = one + timedelta(days=3)
    five = one + timedelta(days=4)
    six = one + timedelta(days=5)
    seven = one + timedelta(days=6)

    qdate = date.today()
   
    context = {'oned':one.strftime('%A'), 'twod':two.strftime('%A'), 'threed':three.strftime('%A'), 'fourd':four.strftime('%A'), 'fived':five.strftime('%A'), 'sixd':six.strftime('%A'), 'sevend':seven.strftime('%A'),
    'one':one, 'two':two, 'three':three, 'four':four, 'five':five, 'six':six, 'seven':seven,
    'qdate':qdate}

    if request.method == 'POST':
            qdate = request.POST['selectdate']
            request.session['qdate'] = qdate
            return redirect('/pages/createOrder')



    #         order_instance = OrderObject()
    #         order_instance.date = qdate
    #         order_instance.save()
    #         # order_instance = OrderObject.objects.create(date=qdate)
    #         form = OrderObjectEditFormDate(instance = order_instance)
    #         context.update({'form':form})

    # if 'orderSubmit' in request.POST:
    #     form = OrderObjectEditFormDate(request.POST, request.FILES, instance=order_instance)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/') 
    
    
    # countofitems = OrderObject.objects.filter(date__range=[form.cleaned_data.get('date'), form.cleaned_data.get('date')]).filter(timeslot = form.cleaned_data.get('timeslot')).count()

    # list_times = []
    # for order in OrderObject.objects.filter(date__range=[qdate,qdate]):
    #     for timeobject in order.timeslot:
    #         countofitems = order.filter(timeslot = 'timeobject').count()
    #         if countofitems < 2:
    #             list_times.append('timeobject')
    # form = Search()
    # if request.method == "GET":
    #     form = Search(request.GET)
    #     qdate = Search(request.FILES)
    return render(request, 'pages/selectDate.html', context)

def createOrderObject(request):

    qdate = request.session.get('qdate')
    form = newForm(qdate = qdate)
    if request.method == 'POST':
        form = newForm(request.POST, qdate = qdate)

        if form.is_valid():
            FirstName = form.cleaned_data['FirstName']
            LastName = form.cleaned_data['LastName']
            Email = form.cleaned_data['Email']
            ConfirmNum = form.cleaned_data['ConfirmNum']
            Timeslot = form.cleaned_data['Timeslot']

            print(FirstName)

            order_instance = OrderObject.objects.create()
            order_instance.FirstName = FirstName
            order_instance.LastName = LastName
            order_instance.Email = Email
            order_instance.date = qdate
            order_instance.ConfirmNum = ConfirmNum
            order_instance.timeslot = Timeslot
            order_instance.save()
            return redirect('/')

    # if request.method == 'POST':
    #     order_instance.date = qdate
    #     order_instance.save()
    #     form = OrderObjectEditFormDate(request.POST, instance=order_instance)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')

    # form = OrderObjectForm()
    # if request.method == 'POST':
    #     form = OrderObjectForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         countofitems = OrderObject.objects.filter(date__range=[form.cleaned_data.get('date'), form.cleaned_data.get('date')]).filter(timeslot = form.cleaned_data.get('timeslot')).count()
    #         if countofitems > 1:
    #             return redirect('/')
    #         form.save()
    #         return redirect('/')

    one = date.today()
    two = one + timedelta(days=1)
    three = two + timedelta(days=2)

    context = {'form':form, 'one':one, 'two':two, 'three':three}

    return render(request, 'pages/createOrder.html', context)

def schedule(request):
    startdate = date.today() 
    enddate = startdate + timedelta(days=6)
    day = OrderObject.objects.filter(date__range=[startdate, enddate])

    one = date.today()
    two = one + timedelta(days=1)

    datetwo = date.today()
    if request.method == 'POST':
            datetwo = request.POST['selectdate']

    dayOne = OrderObject.objects.filter(date__range=[datetwo, datetwo]).order_by('timeslot')

    certaintimes = OrderObject.objects.filter(date__range=[datetwo, datetwo]).filter(timeslot = '09:10 – 09:20').order_by('timeslot')

    color = "#f1f1f1"
    context = {'day': day, 'dayOne': dayOne, 'dayTwo': certaintimes, 'color':color,'datetwo':datetwo}

    return render(request, 'pages/schedule.html', context)

def editOrder(request, pk):
    days = OrderObject.objects.get(id=pk)
    form = OrderObjectEditForm(instance = days)

    if request.method == "POST":
        form = OrderObjectEditForm(request.POST, request.FILES, instance=days)
        if form.is_valid():
            form.save()
            return redirect('/')

    color = "#f1f1f1"
    if days.BagPulled == True:
        color = "yellow"
    elif days.BagPickedUp == True:
        color = "green"
    elif days.MissedPickUp == True:
        color = "red"
    elif days.InvalidConfirmNum == True:
        color = "red"

    context = {'color':color,'form':form}
    return render(request, 'pages/editOrder.html', context)

def deleteOrder(request, pk):
    days = OrderObject.objects.get(id=pk)
    if request.method == "POST":
        days.delete()
        return redirect('/')

    context = {'item':days}
    return render(request, 'pages/deleteOrder.html', context)