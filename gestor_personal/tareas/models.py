from django.db import models
from datetime import date
# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=100,blank=False,null=False)
    descripcion = models.TextField(blank=True,null=True)
    date = models.DateField(default=date.today)
    
    
    def __str__(self):
        return self.titulo
        