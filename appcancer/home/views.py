from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from .forms import SignUpForm

# Create your views here.
def index (request):
    return render(request, 'index.html')

#def perfil (request):
#    return render(request, 'login.html')

def directorio (request):
    return render(request, 'directorio.html')

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
        return render(request, 'signup.html', {'form': SignUpForm()})
