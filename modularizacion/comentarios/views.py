from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse('Hola')

def create(request):
    #comment = Comment(name='Jose',score=5,comment='Soy un comentario..')
    #comment.save()
    comment = Comment.objects.create(name='alex')

    return HttpResponse('Ruta para probar la creacion de modelos')

def delete(request):
    #comment = Comment.objects.get(id=3)
    #comment.delete()

    Comment.objects.filter(id=1).delete()
    return HttpResponse('Ruta para eliminar objetos')
    