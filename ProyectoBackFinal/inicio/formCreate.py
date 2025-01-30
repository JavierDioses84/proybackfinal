from django.forms import ModelForm
from .models import Servicios

class ServForm(ModelForm):
    class Meta:
        model = Servicios
        fields = ['ServicioNombre','detalleServicio', 'obsEstado', 'observSesiones']

    

    """
    ServicioNombre = models.CharField(max_length=100)
    detalleServicio = models.TextField(blank=True)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaTermino = models.DateField(null=True)
    estado = models.CharField(max_length=20, default="Registrado") #En atencion, cerrado, cancelado
    obsEstado = models.TextField(blank=True, default="Estado inicia como registrado")
    sesiones = models.IntegerField(default=6)
    observSesiones = models.TextField(blank=True, default="Estado inicia como registrado")
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Eliminar en cascada
    """