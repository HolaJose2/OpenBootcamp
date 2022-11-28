from django.db import models
from datetime import date

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)
    apellido = models.CharField(max_length=50,blank=False,null=False)
    correo = models.EmailField(blank=False,null=False)
    contraseña = models.CharField(max_length=15,blank=False,null=False)
    celular = models.CharField(max_length=15,blank=True,null=True)
    direccion = models.CharField(max_length=150,blank=True,null=True)

    def __str__(self) -> str:
        return self.nombre

