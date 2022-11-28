from django.shortcuts import render,redirect
from .models import Mascota
from .forms import MascotaForm
from django.contrib import messages


# Create your views here.
def index(request):
    mascotas = Mascota.objects.filter(nombre__contains= request.GET.get('search',''))
    context ={
        'mascotas':mascotas
    }
    return render(request,'mascotas/index.html',context)

def view(request,id):
    mascota = Mascota.objects.get(id=id)
    context ={
        'mascota':mascota
    }
    return render(request,'mascotas/detalles.html',context)


def editar(request,id):
    mascota = Mascota.objects.get(id=id)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
        context ={
            'form':form,
            'id': id
        }
        return render(request,'mascotas/editar.html',context)

    if request.method == 'POST':
        form = MascotaForm(request.POST,instance=mascota,files=request.FILES)
        if form.is_valid():
            form.save()
        context ={
            'form':form,
            'id': id
        }
        messages.success(request, 'Mascota Actualizada.')
        context['form'] = MascotaForm(instance=Mascota.objects.get(id=id))

        return render(request,'mascotas/editar.html',context)



def crear(request):
    if request.method =='GET':
        form = MascotaForm()
        context = {
            'form':form
        }
        return render(request,'mascotas/crear.html',context)

    if request.method == 'POST':
        form = MascotaForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('mascota')


def eliminar(request,id): 
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('mascota')

