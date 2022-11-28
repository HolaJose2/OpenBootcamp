from django.db import models
from datetime import date

class Contactos(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=12,blank=True,null=True)
    celular = models.CharField(max_length=12,blank=False,null=False)
    email = models.EmailField()
    compañia = models.CharField(max_length=100,blank=True,null=True)
    fecha_registro = models.DateField(default=date.today)
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.nombre