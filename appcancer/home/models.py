from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
import os.path
import urllib, hashlib
# Create your models here.

class Profile(models.Model):
    is_doctor = models.NullBooleanField(default=False, blank=True)
    is_fundacion=models.NullBooleanField(default=False, blank=True)
    is_hospital=models.NullBooleanField(default=False, blank=True)
    user = models.OneToOneField(User)
    url = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'auth_profile'

    def get_url(self):
        url = self.url
        if "http://" not in self.url and "https://" not in self.url and len(self.url) > 0:
            url = "http://" + str(self.url)
        return url

    def get_picture(self):
        no_picture = 'http://trybootcamp.vitorfs.com/static/img/user.png'
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' + self.user.username + '.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' + self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                gravatar_url = u'http://www.gravatar.com/avatar/{0}?{1}'.format(
                    hashlib.md5(self.user.email.lower()).hexdigest(),
                    urllib.urlencode({'d':no_picture, 's':'256'})
                    )
                return gravatar_url
        except Exception as e:
            return no_picture

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username

    def notify_answered(self, question):
        if self.user != question.user:
            Notification(notification_type=Notification.ANSWERED,
                from_user=self.user,
                to_user=question.user,
                question=question).save()

    def notify_accepted(self, answer):
        if self.user != answer.user:
            Notification(notification_type=Notification.ACCEPTED_ANSWER,
                from_user=self.user,
                to_user=answer.user,
                answer=answer).save()

    def unotify_accepted(self, answer):
        if self.user != answer.user:
            Notification.objects.filter(notification_type=Notification.ACCEPTED_ANSWER,
                from_user=self.user,
                to_user=answer.user,
                answer=answer).delete()
    def get_medical_profile(self):
        doctor_profile = None
        if hasattr(self, 'doctor'):
            doctor_profile = self.doctor
        return doctor_profile

    def get_fundacion_profile(self):
        fundacion_profile = None
        if hasattr(self, 'fundacion'):
            fundacion_profile = self.fundacion
        return fundacion_profile

    def get_hospital_profile(self):
        hospital_profile = None
        if hasattr(self, 'hospital'):
            hospital_profile = self.hospital
        return hospital_profile

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

class Hospital(models.Model):
    user_name = models.OneToOneField(User)
    active = models.BooleanField(default=True)
    nombre = models.CharField(max_length=100,null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    codigopostal=models.IntegerField(null=True, blank=True)
    Direccion = models.CharField(max_length=100,null=True, blank=True)
    def __unicode__(self):
        return self.nombre

class Doctor(models.Model):
    Doctor_user=models.OneToOneField(User)
    active = models.BooleanField(default=True)
    nombre_doc=models.CharField(max_length=100,default='nombre_doc',null=True, blank=True)
    apellidopat_doc=models.CharField(max_length=100,default='apellido_doc',null=True, blank=True)
    apellidomat_doc=models.CharField(max_length=100,default='apellido_doc',null=True, blank=True)
    titulos=models.TextField(null=True, blank=True)
    cedulatitulacion=models.CharField(max_length=100,null=True, blank=True)
    idFundacion_user=models.ForeignKey(Hospital)
    def __unicode__(self):
        return self.name.Doctor_user

class Noticia(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.IntegerField()
    cotenido=models.IntegerField()
    imagen = models.CharField(max_length=100)
    fechapublicacion=models.DateField(blank=True,null=True)

    def __unicode__(self):
        return self.titulo


class Fundacion(models.Model):
    user_name = models.OneToOneField(User)
    active = models.BooleanField(default=True)
    nombre = models.CharField(max_length=100,null=True, blank=True)
    direccion = models.CharField(max_length=150,null=True, blank=True)
    cuentabancaria=models.IntegerField(null=True, blank=True)
    numerotelefono = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.nombre


#no se si se deberia de agregar un modelo para cuando se hacen citas
#y otro para hacer los mensajes entre paciente y medico
