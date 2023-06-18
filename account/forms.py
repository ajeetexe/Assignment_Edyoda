from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class ResgisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=1000,widget=forms.PasswordInput)

