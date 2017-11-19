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
