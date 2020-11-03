from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import CompanyInfo
from django.shortcuts import get_object_or_404


def index(request):
    if request.method == 'POST':
        if request.POST.get('signup'):
            CompanyInfo.objects.create(name_of_company=request.POST.get('comp_name'),
                                       email_of_company=request.POST.get('comp_email'),
                                       password_of_company=request.POST.get('comb_pass'),
                                       activation_code=request.POST.get('activation_code'))
            return render(request, 'main/home.html', {})
        elif request.POST.get('signin'):
            print("i'm hereeeee")
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            try:
                query = CompanyInfo.objects.get(email_of_company=username)
                print(username+"in try")
            except Exception as e:
                return redirect('403')
            if query.password_of_company == password:
                return redirect('home')
            else:
                print("Someone tried to login and failed.")
                return redirect('403')

    elif request.method == 'GET':
        return render(request, 'main/index.html', {})


def home(request):
    return render(request, "main/home.html", {})


def page403(request):
    return render(request, "main/page403.html", {})

