from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
    return render(request,'form.html',{})


def getgoal(request):
    if request.method != 'GET':
        return HttpResponse("El metodo post no está soportado")
    nombre = request.GET['nombre']
    return render(request,'success.html',{'nombre':nombre})


def postform(request):
    return render(request,'postform.html',{})
    


def postgoal(request):
    if request.method !="POST":
        return HttpResponse("metodo get no está soportado")
    info = request.POST['info']
    return render(request,'postsuccess.html',{'info':info})

