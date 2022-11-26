from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Entry

def update(request):
    author = Author.objects.get(id=1)
    author.name = 'Jose'
    author.email ='mono28h@gmail.com'
    author.save()

    return HttpResponse('Usuario modificado')

def queries(request):
    #Obtener todos los elementos
    authors = Author.objects.all()

    #Obtener datos filtrados por condicion
    authorfilter = Author.objects.filter(email='kyle10@example.org')

    #Obtener un unico objeto
    filters = Author.objects.get(id=1)
    
    #Obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    #obtener 10 objetos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    #obtener elementos ordenados
    orders = Author.objects.all().order_by('email')
    
    #obtener elementos cuyo id sea menor o igual a 15
    filters2 = Author.objects.filter(id__lte=15)

    #obtener todos los autores que contienen en su nombre la palabra yes
    contain = Author.objects.filter(name__contains="require")

    return render(request,'post/queries.html',{'authors':authors,'authorfilter':authorfilter,'filters':filters,'limits':limits,'offsets':offsets,'orders':orders,'filters2':filters2,'contain':contain})


