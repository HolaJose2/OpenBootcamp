from django.contrib import admin
from .models import Mascota,EstadoMascota,Raza,HogarPaso
# Register your models here.
admin.site.register(Mascota)
admin.site.register(EstadoMascota)
admin.site.register(Raza)
admin.site.register(HogarPaso)
