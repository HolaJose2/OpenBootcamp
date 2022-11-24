from django.shortcuts import render
from django.http import HttpResponse

def herencia(request):
    return render(request,'herencia.html',{})

def ejemplo(request):
    return render(request,'ejemplo.html',{})

def otra(request):
    return render(request,'otra.html',{})
    
def index(request):
    return render(request,'index.html',{})