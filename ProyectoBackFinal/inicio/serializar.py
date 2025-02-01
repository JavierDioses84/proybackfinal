from rest_framework import serializers
from inicio.models import Servicios


class ServSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'
        read_only_fields = ('ServicioNombre', 'fechaInicio', 'fechaTermino', 'estado', 'Usuario')
