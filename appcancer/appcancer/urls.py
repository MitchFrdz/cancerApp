"""appcancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from home.views import index, signup, inicio, directorio,nosotros,reportehospital,reportemedicos,reporteasociacion,directorios
from django.conf import settings
from django.contrib.auth.views import login, logout_then_login# auth_views
from django.contrib.auth import views as auth_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name='inicio'),
    url(r'^index/$', index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^directorio/', directorio, name='directorio'),
     url(r'^nosotros/', nosotros, name='nosotros'),
    #url(r'^login/', login, name='login'),
    url(r'^login/$', auth_view.login, {'template_name':'perfil.html'}, name= "login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^signup/$', signup, name="signup"),
    url(r'^directorio/',directorios.as_view(),name="directorio"),
    url(r'^doctores/',reportemedicos.as_view(),name="reportedoctores"),
    url(r'^fundacion/',reporteasociacion.as_view(),name="reportefundacion"),
    url(r'^hospital/',reportehospital.as_view(),name="reporte_hospital"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
