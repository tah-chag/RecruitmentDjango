from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from ChatterBot-master import chatterbot

# Create your views here.
def home(request):
    return render(request, 'recruitment/login.html', args)
#define the register form
def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form_is_valid():
            form.save()
            return redirect('/recruitment')
            else
            form = UserCreationForm()

            args = {'form': form}
            return render(request, 'recruitment/regform.html', args)
#define the login form
def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request.POST)
        if form_is_valid():
            form.save()
            return redirect('/recruitment')
            else
            form = AuthenticationForm()

            args = {'form': form}
            return render(request, 'recruitment/login.html')
