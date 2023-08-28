from django.shortcuts import render

from django.views.generic import TemplateView, UpdateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .forms import *
from .models import *

from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'app/base1.html'
    
def home2(request):
    return render(request, "app/base2.html")

def detalles(request):
    return render(request, "app/base_detalles.html")

#================================Usuario====================================================

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password = password)
            if user is not None:
                login(request, user) 
                return render(request, "app/base1.html", {'form':form})
            else:
                return render(request, "app/login.html", {'form':form, 'mensaje':"Usuario o contraseña incorrectos"})
        else:
            return render(request, "app/login.html", {'form':form, 'mensaje':"Usuario o contraseña incorrectos"})
    form = AuthenticationForm()
    return render(request, 'app/login.html', {'form':form})

def registerUser(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')
        form.save()
        return render(request, "app/registered.html", {'user': usuario}) 
    else: 
     form = UserRegisterForm()
        
    return render(request, "app/register.html", {'form' : form})

class UsuarioEdicion(LoginRequiredMixin, UpdateView):
    form_class = UserEditForm
    template_name= 'app/edit_user.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
#================================Componentes====================================================

#_________________________________Procesador_____________________________________________________

class ProcesadorLista(LoginRequiredMixin, ListView):
    context_object_name = 'procesadores'
    queryset = Componente.objects.filter(componente__startswith='procesador')
    template_name = 'app/procesador_lista.html'
    
class ProcesadorVer(LoginRequiredMixin, DetailView):
    model = Componente
    context_object_name = 'procesador'
    template_name = 'app/procesador_ver.html'