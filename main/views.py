from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .templates.forms import SignUpForm


def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("They used username: {} and password: {}".format(username, password))
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'main/index.html', {})


def home(request):
    return render(request, "main/home.html", {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/home.html', {'form': form})

