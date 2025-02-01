"""
URL configuration for ProyectoBackFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inicio import views

#from django.urls import re_path
#from rest_framework import permissions
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi
'''
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.signin, name='login'),
    path('', views.signin),
    path('signup/', views.signup),
    path('home/', views.home, name='home'),
    path('finanzas/', views.asesFin),
    path('contacto/', views.contacto),
    path('gestproc/', views.gestProc),
    path('intelnegocio/', views.intelNeg),
    #path('api/', include('inicio.urls')),
    path('logout/', views.signout, name='logout'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/crear/', views.crear_Servicios, name='crear_serv'),
    path('servicios/lista/', views.lista_servicios, name='lista_serv'),
    path('servicios/listaR/', views.lista_serviciosR, name='lista_servR'), #Registrados
    path('servicios/listaAt/', views.lista_serviciosAt, name='lista_At'), #Atendiendo
    path('servicios/listaC/', views.lista_serviciosC, name='lista_C'), #Cerrados
    path('servicios/<int:serv_id>/', views.detalle_servicio, name='det_serv'),
    path('servicios/<int:serv_id>/asignar', views.asignar_servicio, name='asig_serv'),
    path('servicios/<int:serv_id>/cerrar', views.cerrar_servicio, name='cerrar_serv'),
    path('servicios/<int:serv_id>/eliminar', views.eliminar_servicio, name='elim_serv'),
    path('nosotros/', views.nosot, name='nosotros'),
    #path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    #path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    #path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
]
