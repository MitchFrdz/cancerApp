from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.forms import ModelForm

class Usuario_Form(UserCreationForm):
    Telefono = forms.IntegerField()
    Correo = forms.CharField(max_length = 50)
    Direccion = forms.CharField(max_length = 100)
