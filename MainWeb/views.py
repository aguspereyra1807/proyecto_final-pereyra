from django.shortcuts import render

from django.views.generic import TemplateView, UpdateView, ListView, DetailView, DeleteView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .forms import *
from .models import *

from django.urls import reverse_lazy

#================================Home====================================================

#class HomeView(TemplateView):
    #template_name = 'app/base1.html'
    
class ComponentesView(TemplateView):
    template_name = 'app/componentes.html'

class SucursalLista(ListView):
    template_name = 'app/base1.html'
    model = Sucursal
    context_object_name = 'sucursales'
    queryset = Sucursal.objects.all
    
#def home2(request):
#    return render(request, "app/base2.html") #no se usa(solo para ver el template base)

#def detalles(request):
#    return render(request, "app/base_detalles.html") #no se usa(solo para ver el template base)

#def index(request):
#    return render(request, "app/index.html") #no se usa(solo para ver el template base)

#================================Usuario====================================================

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = password)
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
            mensaje = "No se pudo registar el usuario"
            return render(request, "app/register.html", {'form' : form, 'mensaje' : mensaje},)
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

class ComponenteAdd(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('home')
    model = Componente
    form_class = ComponenteAddForm
    template_name = 'app/componente_agregar.html'
    
class ComentarioAdd(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ComentarioForm
    template_name = 'app/comentario_agregar.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.componenteAsociado_id = self.kwargs['pk']
        return super(ComentarioAdd, self).form_valid(form)
    
#_________________________________Procesador_____________________________________________________

class ProcesadorLista(LoginRequiredMixin, ListView):
    context_object_name = 'procesadores'
    queryset = Componente.objects.filter(componente__startswith='procesador')
    template_name = 'app/procesador_lista.html'
    
class ProcesadorDetalles(LoginRequiredMixin, DetailView):
    model = Componente
    context_object_name = 'procesador'
    template_name = 'app/procesador_detalles.html'
    
class ProcesadorEditar(LoginRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteEditForm
    success_url = reverse_lazy('procesadores_lista')
    context_object_name = 'procesador'
    template_name = 'app/procesador_editar.html'
    
class ProcesadorEliminar(LoginRequiredMixin, DeleteView):
    model = Componente
    success_url = reverse_lazy('procesadores_lista')
    context_object_name = 'procesador'
    template_name = 'app/procesador_eliminar.html'

#_________________________________Placa de Video_____________________________________________________

class PlacaVideoLista(LoginRequiredMixin, ListView):
    context_object_name = 'placa_video'
    queryset = Componente.objects.filter(componente='placa_video')
    template_name = 'app/placa_video_lista.html'
    
class PlacaVideoDetalles(LoginRequiredMixin, DetailView):
    model = Componente
    context_object_name = 'placa_video'
    template_name = 'app/placa_video_detalles.html'
    
class PlacaVideoEditar(LoginRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteEditForm
    success_url = reverse_lazy('placa_video_lista')
    context_object_name = 'placa_video'
    template_name = 'app/placa_video_editar.html'
    
class PlacaVideoEliminar(LoginRequiredMixin, DeleteView):
    model = Componente
    success_url = reverse_lazy('placa_video_lista')
    context_object_name = 'placa_video'
    template_name = 'app/placa_video_eliminar.html'
    
#_________________________________Motherboards_____________________________________________________

class MotherboardLista(LoginRequiredMixin, ListView):
    context_object_name = 'motherboard'
    queryset = Componente.objects.filter(componente='motherboard')
    template_name = 'app/motherboard_lista.html'
    
class MotherboardDetalles(LoginRequiredMixin, DetailView):
    model = Componente
    context_object_name = 'motherboard'
    template_name = 'app/motherboard_detalles.html'
    
class MotherboardEditar(LoginRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteEditForm
    success_url = reverse_lazy('motherboard_lista')
    context_object_name = 'motherboard'
    template_name = 'app/motherboard_editar.html'
    
class MotherboardEliminar(LoginRequiredMixin, DeleteView):
    model = Componente
    success_url = reverse_lazy('motherboard_lista')
    context_object_name = 'motherboard'
    template_name = 'app/motherboard_eliminar.html'

#_________________________________RAM_____________________________________________________

class RamLista(LoginRequiredMixin, ListView):
    context_object_name = 'ram'
    queryset = Componente.objects.filter(componente='ram')
    template_name = 'app/ram_lista.html'
    
class RamDetalles(LoginRequiredMixin, DetailView):
    model = Componente
    context_object_name = 'ram'
    template_name = 'app/ram_detalles.html'
    
class RamEditar(LoginRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteEditForm
    success_url = reverse_lazy('ram_lista')
    context_object_name = 'ram'
    template_name = 'app/ram_editar.html'
    
class RamEliminar(LoginRequiredMixin, DeleteView):
    model = Componente
    success_url = reverse_lazy('ram_lista')
    context_object_name = 'ram'
    template_name = 'app/ram_eliminar.html'
    
#_________________________________Gabinetes_____________________________________________________

class GabineteLista(LoginRequiredMixin, ListView):
    context_object_name = 'gabinete'
    queryset = Componente.objects.filter(componente='gabinete')
    template_name = 'app/gabinete_lista.html'
    
class GabineteDetalles(LoginRequiredMixin, DetailView):
    model = Componente
    context_object_name = 'gabinete'
    template_name = 'app/gabinete_detalles.html'
    
class GabineteEditar(LoginRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteEditForm
    success_url = reverse_lazy('gabinete_lista')
    context_object_name = 'gabinete'
    template_name = 'app/gabinete_editar.html'
    
class GabineteEliminar(LoginRequiredMixin, DeleteView):
    model = Componente
    success_url = reverse_lazy('gabinete_lista')
    context_object_name = 'gabinete'
    template_name = 'app/gabinete_eliminar.html'
    
#_________________________________Otros_____________________________________________________

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otro'
    queryset = Componente.objects.filter(componente='otro')
    template_name = 'app/otro_lista.html'
    
class OtroDetalles(LoginRequiredMixin, DetailView):
    model = Componente
    context_object_name = 'otro'
    template_name = 'app/otro_detalles.html'
    
class OtroEditar(LoginRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteEditForm
    success_url = reverse_lazy('otro_lista')
    context_object_name = 'otro'
    template_name = 'app/otro_editar.html'
    
class OtroEliminar(LoginRequiredMixin, DeleteView):
    model = Componente
    success_url = reverse_lazy('otro_lista')
    context_object_name = 'otro'
    template_name = 'app/otro_eliminar.html'
    
#================================Componentes====================================================

class SucursalesDetalles(LoginRequiredMixin, DetailView):
    model = Sucursal
    context_object_name = 'sucursal'
    template_name = 'app/sucursal_detalles.html'