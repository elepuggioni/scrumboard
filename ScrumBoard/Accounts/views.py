from django.shortcuts import render
from django.http import HttpResponse
from ScrumBoard import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def home(request):
    return render(request, 'dashboard.html')

def profilo(request):
    return render(request, 'profilo.html')