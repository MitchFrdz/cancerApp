from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView
from .models import Usuario
from .forms import Usuario_Form

# Create your views here.
def index (request):
    return render(request, 'index.html')
def login (request):
    return render(request, 'login.html')

class Signup(FormView):
    template_name = 'signup.html'
    form_class = Usuario_Form
    success_url = reverse_lazy('login')

def form_valid(self, form):
    user = form.save()
    p = Usuario()
    p.Nombre = user
    p.Telefono = form.cleaned_data['Telefono']
    p.Correo = form.cleaned_data['Correo']
    p.Direccion = form.cleaned_data['Direccion']

    p.save()
    return super(Signup, self).form_valid(form)
