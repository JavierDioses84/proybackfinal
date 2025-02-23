# Generated by Django 5.1.5 on 2025-01-27 17:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServicioNombre', models.CharField(max_length=100)),
                ('detalleServicio', models.TextField(blank=True)),
                ('fechaInicio', models.DateTimeField(auto_now_add=True)),
                ('fechaTermino', models.DateField(null=True)),
                ('estado', models.CharField(default='Registrado', max_length=20)),
                ('obsEstado', models.TextField(blank=True, default='Estado inicia como registrado')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
