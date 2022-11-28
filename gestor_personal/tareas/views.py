from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea
from .forms import TareasForm
from django.contrib import messages
# Create your views here.
def index(request):
    tareas = Tarea.objects.filter(titulo__contains= request.GET.get('search',''))
    context ={
        'tareas':tareas
    }
    return render(request,'tarea/index.html',context)

def view(request,id):
    tarea = Tarea.objects.get(id=id)
    context ={
        'tarea':tarea
    }
    
    return render(request,'tarea/detalles.html',context)


def editar(request,id):
    tarea = Tarea.objects.get(id=id)
    if request.method == 'GET':
        form = TareasForm(instance=tarea)
        context ={
            'form':form,
            'id': id
        }
        return render(request,'tarea/editar.html',context)

    if request.method == 'POST':
        form = TareasForm(request.POST,instance=tarea)
        if form.is_valid():
            form.save()
        context ={
            'form':form,
            'id': id
        }
        messages.success(request, 'Tarea Actualizada.')

        return render(request,'tarea/editar.html',context)



def crear(request):
    if request.method =='GET':
        form = TareasForm()
        context = {
            'form':form
        }
        return render(request,'tarea/crear.html',context)

    if request.method == 'POST':
        form = TareasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tarea')



def eliminar(request,id): 
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('tarea')
