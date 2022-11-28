from django.shortcuts import render,redirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages


# Create your views here.
def index(request):
    usuarios = Usuario.objects.filter(nombre__contains= request.GET.get('search',''))
    context ={
        'usuarios':usuarios
    }
    return render(request,'usuarios/index.html',context)

def view(request,id):
    usuario = Usuario.objects.get(id=id)
    context ={
        'usuario':usuario
    }
    return render(request,'usuarios/detalles.html',context)


def editar(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
        context ={
            'form':form,
            'id': id
        }
        return render(request,'usuarios/editar.html',context)

    if request.method == 'POST':
        form = UsuarioForm(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
        context ={
            'form':form,
            'id': id
        }
        messages.success(request, 'Usuario Actualizado.')

        return render(request,'usuarios/editar.html',context)



def crear(request):
    if request.method =='GET':
        form = UsuarioForm()
        context = {
            'form':form
        }
        return render(request,'usuarios/crear.html',context)

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usuario')



def eliminar(request,id): 
    tarea = Usuario.objects.get(id=id)
    tarea.delete()
    return redirect('usuario')
