from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from .forms import ServForm
from .models import Servicios

# Create your views here.



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
           # Registrar usuarios
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()  # guardar en la base de datos
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form' : UserCreationForm,
                    'error' : "Usuario ya existe"
                })


        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('login')


def signin(request):
    if request.method == 'GET':
        return render(request, 'inicio.html', {
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'inicio.html', {
                'form' : AuthenticationForm,
                'error' : 'Usuario o password incorrecto'
            })
        else:
            login(request, user)
            return redirect('home')

@login_required
def crear_Servicios(request):
    if request.method == 'GET':
        return render(request, 'crearServicios.html', {
            'form' : ServForm
        })
    else:
        try:
            form = ServForm(request.POST)
            nuevoServ = form.save(commit=False)
            nuevoServ.Usuario = request.user
            nuevoServ.save()
            return redirect('servicios')
        except ValueError:
            return render(request, 'crearServicios.html', {
            'form' : ServForm,
            'error' : 'Ingresar datos validos'
        })
        """
        return render(request, 'crearServicios.html', {
            'form' : ServForm
        }) """

@login_required
def lista_servicios(request):
    if request.user.is_superuser:
        servs =  Servicios.objects.filter()
    else:
        servs =  Servicios.objects.filter(Usuario=request.user, fechaTermino__isnull=True)
    return render(request, 'listaServicios.html', {'servs' : servs})

'''
def cerrar_servicio(request, serv_id):
    if request.user.is_superuser:
        serv = get_object_or_404(Servicios, pk=serv_id)
        if request.method == 'POST':
            serv.fechaTermino = timezone.now()
            serv.estado = 'Cerrado'
            serv.obsEstado = serv.obsEstado + ', servicio cerrado'
            serv.save()
            return redirect('lista_serv')
    else:
        return render(request, 'detalleServicios.html', {'error3' : 'Asigna solo el administrador'})
    
def delete_servicio(request, serv_id):
    if request.user.is_superuser:
        serv = get_object_or_404(Servicios, pk=serv_id)
        if request.method == 'POST':
            serv.fechaTermino = timezone.now()
            serv.estado = 'Cerrado'
            serv.obsEstado = serv.obsEstado + ', servicio cerrado'
            serv.save()
            return redirect('lista_serv')
    else:
        return render(request, 'detalleServicios.html', {'error4' : 'Asigna solo el administrador'})
'''

@login_required
def detalle_servicio(request, serv_id):
    if request.method == 'GET':
        if request.user.is_superuser:
            serv =  get_object_or_404(Servicios, pk=serv_id)
        else:
            serv =  get_object_or_404(Servicios, pk=serv_id, Usuario=request.user)
        form = ServForm(instance=serv)
        return render(request, 'detalleServicio.html', {'serv' : serv, 'form' : form})
    else:
        try:
            if request.user.is_superuser:
                serv =  get_object_or_404(Servicios, pk=serv_id)
            else:
                serv =  get_object_or_404(Servicios, pk=serv_id, Usuario=request.user)
            form = ServForm(request.POST, instance=serv)
            form.save() #Actualizar BD
            return redirect('lista_serv')
        except ValueError:
            return render(request, 'detalleServicio.html', {'serv' : serv, 'form' : form, 'error' : "Error al actualizar los datos"})

@login_required
def asignar_servicio(request, serv_id):
    serv = get_object_or_404(Servicios, pk=serv_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            serv.fechaTermino = timezone.now()
            serv.estado = 'En atención'
            serv.obsEstado = serv.obsEstado + ', actualmente en atención'
            serv.save()
            return redirect('lista_serv')
    else:
        return render(request, 'detalleServicio.html', {'serv' : serv, 'error2' : "Solo el usuario administrador asigna"})

@login_required
def cerrar_servicio(request, serv_id):
    serv = get_object_or_404(Servicios, pk=serv_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            serv.fechaTermino = timezone.now()
            serv.estado = 'Cerrado'
            serv.obsEstado = serv.obsEstado + ', servicio cerrado y entregado'
            serv.save()
            return redirect('lista_serv')
    else:
        form = ServForm(instance=serv)
        return render(request, 'detalleServicio.html', {'serv' : serv, 'form' : form, 'error3' : "Solo el usuario administrador cierra"})

@login_required
def eliminar_servicio(request, serv_id):
    serv = get_object_or_404(Servicios, pk=serv_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            serv.delete()
            return redirect('lista_serv')
    else:
        form = ServForm(instance=serv)
        return render(request, 'detalleServicio.html', {'serv' : serv, 'form' : form, 'error4' : "Solo el usuario administrador elimina"})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def asesFin(request):
    return render(request, 'asesorfinanzas.html')

@login_required
def contacto(request):
    return render(request, 'contacto.html')

@login_required
def gestProc(request):
    return render(request, 'gestprocesos.html')

@login_required
def intelNeg(request):
    return render(request, 'intelnegocio.html')

@login_required
def nosot(request):
    return render(request, 'nosotros.html')

@login_required
def servicios(request):
    return render(request, 'servicios.html')