# onboarding/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'onboarding/index.html')

def identify(request):
    return render(request, 'onboarding/identify.html')