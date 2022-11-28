from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='contacto'),
    path('view/<int:id>',views.viewContacto,name='viewContacto'),
    path('editar/<int:id>',views.editar,name='editarContacto'),
    path('crear/',views.crear,name='crearContacto'),
    path('eliminar/<int:id>',views.eliminar,name='eliminarContacto'),



]