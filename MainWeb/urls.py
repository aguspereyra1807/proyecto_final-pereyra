from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('componentes/', ComponentesView.as_view(), name="componentes"),
    path('', SucursalLista.as_view(), name="home"),
    #path('', HomeView.as_view(), name="home"),
    #path('home2/', home2, name="home2"), #no se usa (solo para ver el html base)
    #path('detalles/', detalles, name="detalles"), #no se usa (solo para ver el html base)
    #path('index/', index, name="index"), #no se usa (solo para ver el html base)
    
    path('componente_agregar/', ComponenteAdd.as_view(), name="componente_agregar"),
    
    path('login/', loginUser, name="login"),
    path('logout/', LogoutView.as_view(template_name="app/logout.html"), name="logout"),
    path('register/', registerUser, name="register"),
    path('edit_user/', UsuarioEdicion.as_view(template_name="app/user_edit.html"), name="edit_user"),

    path('procesadores_lista/', ProcesadorLista.as_view(), name="procesadores_lista"),
    path('procesadores_detalles/<int:pk>', ProcesadorDetalles.as_view(), name="procesadores_detalles"),
    path('procesadores_detalles/<int:pk>/comentario_agregar', ComentarioAdd.as_view(), name="comentario_agregar"),
    path('procesadores_editar/<int:pk>', ProcesadorEditar.as_view(), name="procesadores_editar"),
    path('procesadores_eliminar/<int:pk>', ProcesadorEliminar.as_view() , name="procesadores_eliminar"),
    
    path('placa_video_lista/', PlacaVideoLista.as_view(), name="placa_video_lista"),
    path('placa_video_detalles/<int:pk>', PlacaVideoDetalles.as_view(), name="placa_video_detalles"),
    path('placa_video_detalles/<int:pk>/comentario_agregar', ComentarioAdd.as_view(), name="comentario_agregar"),
    path('placa_video_editar/<int:pk>', PlacaVideoEditar.as_view(), name="placa_video_editar"),
    path('placa_video_eliminar/<int:pk>', PlacaVideoEliminar.as_view() , name="placa_video_eliminar"),
    
    path('motherboard_lista/', MotherboardLista.as_view(), name="motherboard_lista"),
    path('motherboard_detalles/<int:pk>', MotherboardDetalles.as_view(), name="motherboard_detalles"),  
    path('motherboard_detalles/<int:pk>/comentario_agregar', ComentarioAdd.as_view(), name="comentario_agregar"),  
    path('motherboard_editar/<int:pk>', MotherboardEditar.as_view(), name="motherboard_editar"),
    path('motherboard_eliminar/<int:pk>', MotherboardEliminar.as_view() , name="motherboard_eliminar"),
    
    path('ram_lista/', RamLista.as_view(), name="ram_lista"),
    path('ram_detalles/<int:pk>', RamDetalles.as_view(), name="ram_detalles"),  
    path('ram_detalles/<int:pk>/comentario_agregar', ComentarioAdd.as_view(), name="ram_agregar"),  
    path('ram_editar/<int:pk>', RamEditar.as_view(), name="ram_editar"),
    path('ram_eliminar/<int:pk>', RamEliminar.as_view() , name="ram_eliminar"),
    
    path('gabinete_lista/', GabineteLista.as_view(), name="gabinete_lista"),
    path('gabinete_detalles/<int:pk>', GabineteDetalles.as_view(), name="gabinete_detalles"),  
    path('gabinete_detalles/<int:pk>/comentario_agregar', ComentarioAdd.as_view(), name="gabinete_agregar"),  
    path('gabinete_editar/<int:pk>', GabineteEditar.as_view(), name="gabinete_editar"),
    path('gabinete_eliminar/<int:pk>', GabineteEliminar.as_view() , name="gabinete_eliminar"),
    
    path('otro_lista/', OtroLista.as_view(), name="otro_lista"),
    path('otro_detalles/<int:pk>', OtroDetalles.as_view(), name="otro_detalles"),  
    path('otro_detalles/<int:pk>/comentario_agregar', ComentarioAdd.as_view(), name="otro_agregar"),  
    path('otro_editar/<int:pk>', OtroEditar.as_view(), name="otro_editar"),
    path('otro_eliminar/<int:pk>', OtroEliminar.as_view() , name="otro_eliminar"),
    
    path('sucursal_detalles/<int:pk>', SucursalesDetalles.as_view(), name="sucursal_detalles"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)