from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

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