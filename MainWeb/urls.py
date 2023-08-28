from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home2/', home2, name="home2"),
    path('detalles/', detalles, name="detalles"),
    
    path('login/', loginUser, name="login"),
    path('logout/', LogoutView.as_view(template_name="app/logout.html"), name="logout"),
    path('register/', registerUser, name="register"),
    path('edit_user/', UsuarioEdicion.as_view(template_name="app/user_edit.html"), name="edit_user"),

    path('procesadores_lista/', ProcesadorLista.as_view(), name="procesadores_lista"),
    path('procesadores_ver/<int:pk>', ProcesadorVer.as_view(), name="procesadores_ver"),
    path('procesadores_editar/', home2, name="procesadores_editar"),
    path('procesadores_eliminar/', home2 , name="procesadores_eliminar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)