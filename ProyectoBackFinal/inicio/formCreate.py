from django.forms import ModelForm
from .models import Servicios

class ServFormCr(ModelForm):
    class Meta:
        model = Servicios
        fields = ['ServicioNombre','detalleServicio', 'obsEstado', 'observSesiones']