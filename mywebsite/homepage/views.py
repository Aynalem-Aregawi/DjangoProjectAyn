from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Index.html')

def intro(request):
    return render(request, 'Intro.html')

def arch(request):
    return render(request, 'Arch.html')

def appl(request):
    return render(request, 'Appl.html')

def proto(request):
    return render(request, 'Proto.html')

def chall(request):
    return render(request, 'Chall.html')
