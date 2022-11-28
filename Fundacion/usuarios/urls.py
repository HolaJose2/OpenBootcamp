from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='usuario'),
    path('view/<int:id>',views.view,name='viewUsuario'),
    path('editar/<int:id>',views.editar,name='editarUsuario'),
    path('crear/',views.crear,name='crearUsuario'),
    path('eliminar/<int:id>',views.eliminar,name='eliminarUsuario'),
]