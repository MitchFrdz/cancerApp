import os
from PIL import Image
from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from .forms import SignUpForm, ProfileForm, Hospital_Form, Fundacion_Form, Doctor_Form
from django.contrib import messages
from django.conf import settings as django_settings

from django.views.generic import ListView
from .models import Hospital
from .models import Fundacion
from .models import Doctor
from .models import Noticia

class directorios(ListView):
    template_name = "directorio.html"
    model = Hospital

class reporteasociacion(ListView):
    template_name = "Fundaciones.html"
    model = Fundacion

class reportemedicos(ListView):
    template_name = "Doctores.html"
    model = Doctor

class reporte_noticia(ListView):
    template_name = "Noticias.html"
    model = Noticia

class reportehospital(ListView):
    template_name = "hospitales.html"
    model = Hospital



# Create your views here.
def index (request):
    return render(request, 'index.html')

#def perfil (request):
#    return render(request, 'login.html')


def directorio (request):
    users_list = User.objects.filter(is_active=True).order_by('username')
    paginator = Paginator(users_list, 100)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'directorio.html', { 'users': users })

    return render(request, 'directorio.html')

@login_required
def setting(request):
    """    form = ProfileForm
    fields = ['first_name', 'last_name', 'is_doctor', 'is_fundacion', 'is_hospital','']

    """
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.profile.is_doctor = form.cleaned_data.get('doctor')
            user.profile.is_fundacion = form.cleaned_data.get('fundacion')
            user.profile.is_hospital = form.cleaned_data.get('hospital')
            #user.email = form.cleaned_data.get('email')
            user.profile.url = form.cleaned_data.get('url')
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Tu perfil ah sido exitosamente modificado.')
    else:
        form = ProfileForm(instance=user, initial={
            'url': user.profile.url,
            'doctor':user.profile.is_doctor,
            'fundacion':user.profile.is_fundacion,
            'hospital':user.profile.is_hospital
            })
    return render(request, 'setting.html', {'form':form})
@login_required
def profile(request):
    page_user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {
        'page_user': page_user,})

@login_required
def profilesetting(request):
    user = request.user
    if user.profile.is_doctor:
        perfil = user.get_doctor_profile()
        if request.method == 'POST':
            form = Doctor_Form(request.POST)
            if form.is_valid():
                user.doctor.nombre_doc = form.cleaned_data.get('nombre_doc')
                user.doctor.apellidopat_doc = form.cleaned_data.get('apellidopat_doc')
                user.doctor.apellidomat_doc = form.cleaned_data.get('apellidomat_doc')
                user.doctor.titulos = form.cleaned_data.get('titulos')
                user.doctor.cedulatitulacion = form.cleaned_data.get('cedulatitulaciontitulos')
            else:
                form = Doctor_Form(instance=user, initial={
                'nombre_doc':user.doctor.nombre_doc,
                'apellidopat_doc':user.doctor.apellidopat_doc ,
                'titulos':user.doctor.titulos,
                'cedulatitulacion':user.doctor.cedulatitulacion
                })
        print('sdfs1')
        return render(request, 'profilesettings.html', {'form':form})
    if user.profile.is_hospital:
        perfil = user.get_hospital_profile()
        if request.method =='POST':
            form = Hospital_Form(request.POST)
            if form.is_valid():
                user.hospital.nombre = form.cleaned_data.get('nombre')
                user.hospital.telefono = form.cleaned_data.get('telefono')
                user.hospital.codigopostal =form.cleaned_data.get('codigopostal')
                user.hospital.Direccion=form.cleaned_data.get('Direccion')
            else:
                form = Hospital_Form(instance=user, initial={
                'nombre':user.hospital.nombre,
                'telefono':user.hospital.telefono,
                'codigopostal':user.hospital.codigopostal,
                'Direccion':user.hospital.Direccion,
                })
        print('dfs2')
        return render(request, 'profilesettings.html', {'form':form})
    if user.profile.is_fundacion:
        perfil = user.get_fundacion_profile()
        if request.method =='POST':
            form = Fundacion_Form(request.POST)
            if form.is_valid():
                user.fundacion.nombre = form.cleaned_data.get('nombre')
                user.fundacion.numerotelefono = form.cleaned_data.get('numerotelefono')
                user.fundacion.cuentabancaria =form.cleaned_data.get('cuentabancaria')
                user.fundacion.direccion=form.cleaned_data.get('direccion')
            else:
                form = Fundacion_Form(instance=user, initial={
                'nombre':user.fundacion.nombre,
                'numerotelefono':user.fundacion.numerotelefono,
                'cuentabancaria':user.fundacion.cuentabancaria,
                'direccion':user.fundacion.direccion,
                })
        print('sdfg3')
        return render(request, 'profilesettings.html', {'form':form})
    else:
        print('sadsfdsaf')
        return render(request, 'profilesettings.html')


def nosotros (request):
    return render(request, 'nosotros.html')

def contacto (request):
    return render(request, 'contacto.html')

def noticias (request):
    return render(request, 'noticias.html')

def inicio (request):
    return render(request, 'inicio.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form})
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        return render(request, 'signup.html', {'form': SignUpForm()}, {'form2':ProfileForm()})
