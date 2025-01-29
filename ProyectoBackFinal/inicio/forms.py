from django.forms import ModelForm
from .models import Servicios

class ServForm(ModelForm):
    class Meta:
        model = Servicios
        fields = ['ServicioNombre', 'detalleServicio', 'obsEstado']