from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactosForm
from .models import Contactos
from django.contrib import messages




# Create your views here.
def index(request):
    contactos = Contactos.objects.filter(nombre__contains= request.GET.get('search',''))
    
    context ={
        'contactos':contactos
    }
    return render(request,'contacto/index.html',context)



def viewContacto(request,id):
    contacto = Contactos.objects.get(id=id)
    context = {
        'contacto': contacto,
    }
    return render(request,'contacto/detalles.html',context)



def editar(request,id):
    contacto = Contactos.objects.get(id=id)
    if (request.method == 'GET'):
        form = ContactosForm(instance=contacto)
        context ={
            'form':form,
            'id': id
        }
        return render(request,'contacto/editar.html',context)

    if (request.method == 'POST'):  
        form = ContactosForm(request.POST,instance= contacto )
        if form.is_valid():
            form.save()
        
        context ={
            'form':form,
            'id': id
        }
        messages.success(request, 'Contacto Actualizado.')

        return render(request,'contacto/editar.html',context)

def crear(request):
    if (request.method == 'GET'):
        form = ContactosForm()
        context ={
            'form':form
        }
        return render(request,'contacto/crear.html',context)

    if (request.method =='POST'):
        form = ContactosForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('contacto')

def eliminar(request,id):
    contacto = Contactos.objects.get(id=id)
    contacto.delete()
    return redirect('contacto')
