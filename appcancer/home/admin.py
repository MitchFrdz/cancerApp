from django.contrib import admin
from .models import Doctor
from .models import Hospital
from .models import Noticia
from .models import Fundacion

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(Noticia)
admin.site.register(Fundacion)
