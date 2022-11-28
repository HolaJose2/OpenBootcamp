from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='tarea'),
    path('view/<int:id>',views.view,name='view'),
    path('editar/<int:id>',views.editar,name='editarTarea'),
    path('crear/',views.crear,name='crearTarea'),
    path('eliminar/<int:id>',views.eliminar,name='eliminarTarea'),
    
]