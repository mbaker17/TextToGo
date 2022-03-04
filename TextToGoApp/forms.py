from asyncio.windows_events import NULL
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from datetime import date, timedelta

from django.forms import ModelForm
from .models import OrderObject

import datetime as dt

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class OrderObjectForm(ModelForm):
    class Meta:
        model = OrderObject
        fields = ['FirstName','LastName','Email','ConfirmNum','timeslot','date']

class OrderObjectEditForm(ModelForm):
    class Meta:
        model = OrderObject
        fields = ['FirstName','LastName','Email','ConfirmNum','timeslot','date','BagPulled','BagPickedUp','MissedPickUp','InvalidConfirmNum']

class OrderObjectEditFormDate(ModelForm):
    class Meta:
        model = OrderObject
        fields = ['FirstName','LastName','Email','ConfirmNum','timeslot']

class newForm (forms.Form): 
    def __init__(self, *args, **kwargs):
        qdate = kwargs.pop('qdate')
        super(newForm,self).__init__(*args, **kwargs) 

        SEMESTER_CHOICES = (
    
)
        SlotsPerDay = 1

        self.fields['FirstName'] = forms.CharField();
        self.fields['LastName'] = forms.CharField();
        self.fields['Email'] = forms.EmailField();
        self.fields['ConfirmNum'] = forms.IntegerField();
        for x in OrderObject.TIMESLOT_LIST:
            timeX = x[1]
            countofitems = OrderObject.objects.filter(date__range=[qdate, qdate]).filter(timeslot = timeX).count()
            #SEMESTER_CHOICES = SEMESTER_CHOICES + ((countofitems,countofitems),)
            if countofitems < SlotsPerDay:
                SEMESTER_CHOICES = SEMESTER_CHOICES + ((x[0],x[1]),)
        self.fields['Timeslot'] = forms.ChoiceField(choices=SEMESTER_CHOICES,
            widget=forms.Select(attrs={'onchange': 'submit();'}))

    # FirstName = forms.CharField();
    # LastName = forms.CharField();
    # Email = forms.EmailField();
    # ConfirmNum = forms.IntegerField();
    # for x in OrderObject.TIMESLOT_LIST:
    #     timeX = x[1]
    #     countofitems = OrderObject.objects.filter(date__range=[yeet, yeet]).filter(timeslot = timeX).count()
    #     #countofitems = OrderObject.objects.filter(date__range=[date.today(), date.today()]).filter(timeslot = '09:10 – 09:20').count()
    #     print('09:10 – 09:20')
    #     print(str(x))
    #     SEMESTER_CHOICES = SEMESTER_CHOICES + ((countofitems,countofitems),)
    #     SEMESTER_CHOICES = SEMESTER_CHOICES + ((x[0],x[1]),)
    #     #if countofitems < 1:
    #         #SEMESTER_CHOICES = SEMESTER_CHOICES + ((str(x),str(x)),)
    # Timeslot = forms.ChoiceField(choices=SEMESTER_CHOICES,
    #     widget=forms.Select(attrs={'onchange': 'submit();'}))


#SEMESTER_CHOICES = SEMESTER_CHOICES + ((str(x),str(x)),)
#'09:10 – 09:20'