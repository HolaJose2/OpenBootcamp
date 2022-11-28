from django.db import models
from usuarios.models import Usuario
from datetime import date

# Create your models here.
class EstadoMascota(models.Model):
    tipo_estado = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self) :
        return self.tipo_estado

class Raza(models.Model):
    tipo_raza = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self) :
        return self.tipo_raza

class HogarPaso(models.Model):
    nombre = models.CharField(max_length=50, blank=False,null=False)
    direccion = models.CharField(max_length=100, blank=False,null=False)
    telefono = models.CharField(max_length=50, blank=False,null=False)
    tamaño = models.CharField(max_length=50, blank=False,null=False)
    capacidad = models.IntegerField(blank=False,null=False)
    
    def __str__(self) :
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=50, blank=False,null=False)
    edad = models.IntegerField(blank=False,null=False)
    genero = models.CharField(max_length=50, blank=False,null=False)
    tamaño = models.CharField(max_length=50, blank=False,null=False)
    fecha_adopcion = models.DateField(blank=True,null=True)
    estado_mascota = models.ForeignKey(EstadoMascota,on_delete=models.SET_NULL,null=True)
    raza = models.ForeignKey(Raza,on_delete=models.SET_NULL,null=True,blank=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True)
    hogar_paso = models.ForeignKey(HogarPaso,on_delete=models.SET_NULL,null=True,blank=True)
    imagen = models.ImageField(null=True,blank=True)
    
    def __str__(self) :
        return self.nombre