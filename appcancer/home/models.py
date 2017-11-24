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

    def __unicode__(self):
        return self.name.Doctor_user


class Hospital(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    codigopostal=models.IntegerField()
    Direccion = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name.Nombre


class Noticia(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.IntegerField()
    cotenido=models.IntegerField()
    imagen = models.CharField(max_length=100)
    fechapublicacion=models.DateField(blank=True,null=True)

    def __unicode__(self):
        return self.name.titulo


class Fundaciones(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    cuentabancaria=models.IntegerField()
    numerotelefono = models.IntegerField()

    def __unicode__(self):
        return self.name.nombre


#no se si se deberia de agregar un modelo para cuando se hacen citas
#y otro para hacer los mensajes entre paciente y medico

