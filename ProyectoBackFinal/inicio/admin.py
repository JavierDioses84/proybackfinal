from django.contrib import admin
from .models import Servicios

# Register your models here.
class servAdmin(admin.ModelAdmin):
    readonly_fields = ("fechaInicio",)

admin.site.register(Servicios, servAdmin)