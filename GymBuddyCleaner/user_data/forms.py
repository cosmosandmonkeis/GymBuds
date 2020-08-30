from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SubmitFormData(ModelForm):
    class Meta:
        model = user_data
        fields = ['name','age', 'goal', 'experience', 'city', 'gym_membership', 'sex' ]

class MessageFormData(ModelForm):
    class Meta:
        model = SendMessage
        fields = ['author', 'message']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
