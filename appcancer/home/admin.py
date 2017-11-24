from django.contrib import admin
from .models import Usuario
from .models import Doctores
from .models import Hospital
from .models import Noticia
from .models import Fundaciones

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Doctores)
admin.site.register(Hospital)
admin.site.register(Noticia)
admin.site.register(Fundaciones)
