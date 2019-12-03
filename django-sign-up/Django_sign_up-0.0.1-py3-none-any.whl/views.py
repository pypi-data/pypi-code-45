from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return HttpResponse("Already Registered")
        else:        
            return HttpResponse("successfully Registered")
    else:
        return render(request, "Django_registration/register.html")