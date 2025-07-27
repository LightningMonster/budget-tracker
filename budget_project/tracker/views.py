from django.shortcuts import render

def landing_view(request):
    return render(request, 'tracker/html/landing.html')

def signup_view(request):
    return render(request, 'tracker/html/signup.html')

def login_view(request):
    return render(request, 'tracker/html/login.html')