from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='mascota'),
    path('view/<int:id>',views.view,name='view'),
    path('editar/<int:id>',views.editar,name='editarMascota'),
    path('crear/',views.crear,name='crearMascota'),
    path('eliminar/<int:id>',views.eliminar,name='eliminarMascota'),


    ]