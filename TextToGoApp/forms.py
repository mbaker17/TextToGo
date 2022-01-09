from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import OrderObject

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class OrderObjectForm(ModelForm):
    class Meta:
        model = OrderObject
        fields = '__all__'