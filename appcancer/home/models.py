from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Usuario(models.Model):
    Nombre = models.OneToOneField(User)
    Telefono = models.IntegerField()
    Correo = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name.username


class Doctores(models.Model):
    Doctor_user=models.OneToOneField(User)
    nombre_doc=models.CharField(max_length=200,default='nombre_doc')
    apellidopat_doc=models.CharField(max_length=200,default='apellido_doc')
    apellidomat_doc=models.CharField(max_length=200,default='apellido_doc')
    correo_doc=models.EmailField(max_length=100)
    edad=models.IntegerField()
    titulos=models.TextField()
    cedulatitulacion=models.CharField(max_length=100)
    idFundacion_user=models.ForeignKey(Fundaciones)
    def __unicode__(self):
        return self.name.Doctor_user


class Hospital(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    codigopostal=models.IntegerField()
    Direccion = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name.Nombre
