from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servicios(models.Model):
    SERVICIOS = {
        'Fi' : 'Finanzas',
        'Gp' : 'Procesos',
        'BI' : 'Inteligencia de Negocio'
    }
    ServicioNombre = models.CharField(max_length=100, choices=SERVICIOS)
    detalleServicio = models.TextField(blank=True)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaTermino = models.DateField(null=True)
    estado = models.CharField(max_length=20, default="Registrado") #En atencion, cerrado, cancelado
    obsEstado = models.TextField(blank=True, default="Estado inicia como registrado")
    sesiones = models.IntegerField(default=6)
    observSesiones = models.TextField(blank=True, default="Se realizan 6 sesiones")
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Eliminar en cascada

    def __str__(self):
        return self.detalleServicio + ' - por ' + self.Usuario.username
'''
#En atencion, cerrado, cancelado
class detalleServ(models.Model):
    titulo = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    costoSesion = models.FloatField(default=200)
    numActividades = models.IntegerField(default=4)
    Obs = models.TextField(blank=True, default="Anotar detalles de la sesión")
    Serv = models.ForeignKey(Servicios.id, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' - Actividades ' + self.numActividades
'''