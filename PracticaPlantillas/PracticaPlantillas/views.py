from django.shortcuts import render


def inicio(request):
    return render(request, 'inicio.html',{})

def portafolio(request):
    return render(request, 'portafolio.html',{})