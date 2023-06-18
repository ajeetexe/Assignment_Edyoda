from django.shortcuts import render, redirect
from .forms import ResgisterForm, LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

def register_view(request):
    register_form = ResgisterForm()
    try:
        if request.method == 'POST':
            register_form = ResgisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request,'Registration success')
                return redirect('/account/login/')
            messages.error(request,'Registration failed')
            return redirect('/account/register/')
    except Exception as e:
        print(e)
    return render(request,'register.html',context={'form':register_form})

def login_view(request):
    login_form = LoginForm()
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(
                    username = login_form.cleaned_data['email'],
                    password = login_form.cleaned_data['password']
                )
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login successful')
                    return redirect('/')
                else:
                    messages.error(request,'Login failed')
                    return redirect('/account/login/')
    except Exception as e:
        print(e)
    return render(request, 'login.html',context={'form':login_form})

def logout_view(request):
    logout(request)
    return redirect('/')