from django.forms import ModelForm
from .models import Tarea

class TareasForm(ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'