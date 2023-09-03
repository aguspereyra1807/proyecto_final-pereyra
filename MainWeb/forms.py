from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import  *
from django.utils.translation import gettext_lazy as _

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UserEditForm(UserChangeForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')
        
class ComponenteAddForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ('componente', 'titulo', 'marca', 'precio', 'year', 'descripcion', 'imagenComponente')
        widgets = {
            'componente' : forms.Select(attrs={'class': 'form-control'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'titulo':_('Título'),
            'year':_('Año de lanzamiento'),
            'descripcion':_('Descripción'),
            'imagenComponente':_('Imagen'),
        }

class ComponenteEditForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ('titulo', 'componente', 'marca', 'descripcion', 'year', 'precio', 'imagenComponente')
        widgets = {
            'componente' : forms.Select(attrs={'class': 'form-control'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
           'marca' : forms.TextInput(attrs={'class': 'form-control'}),
           'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
           'year' : forms.TextInput(attrs={'class': 'form-control'}),
           'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
           'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'comentario')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario' : forms.Textarea(attrs={'class': 'form-control'}),
        }