from django.db import models

# Create your models here.

class Componente(models.Model):
	componenteSeleccion = (
    ('procesador', 'Procesador'),
	('placa_video', 'Placa de Video'),
	('motherboard', 'Placa Madre'),
	('gabinete', 'Gabinete'),
	('ram', 'RAM'),
	('almacenamiento', 'Almacenamiento'),
	('otro', 'Otro'))
	componente = models.CharField(max_length=20, choices=componenteSeleccion, default='procesador')
	titulo = models.CharField(max_length=60)
	marca = models.CharField(max_length=40)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	imagenComponente = models.ImageField(null=True, blank=True,upload_to='imagenes/')
	year = models.CharField(max_length=40)
	descripcion = models.TextField(null=True, blank=True)
	fechaPublicacion = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-fechaPublicacion']

	def __str__(self):
		return self.titulo
  
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    comentario = models.CharField(max_length=250)
    fechaComentario = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fechaComentario']
        
    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    provinciaSeleccion = (('buenos_aires','Buenos Aires'),
						  ('catamarca','Catamarca'),
						  ('chaco','Chaco'),
						  ('chubut','Chubut'),
						  ('cordoba','Córdoba'),
						  ('corrientes','Corrientes'),
						  ('entre_rios','Entre Rios'),
						  ('formosa','Formosa'),
						  ('jujuy','Jujuy'),
						  ('la_pampa','La Pampa'),
						  ('la_rioja','La Rioja'),
						  ('mendoza','Mendoza'),
						  ('neuquen','Neuquén'),
						  ('rio_negro','Rio Negro'),
						  ('salta','Salta'),
						  ('san_juan','San Juan'),
						  ('santa_luis','Santa Luis'),
						  ('santa_cruz','Santa Cruz'),
						  ('santa_fe','Santa Fe'),
						  ('santiago_del_estero','Santiago del Estero'),
						  ('tierra_de_fuego','Tierra de Fuego'),
						  ('tucuman','Tucumán'))
    provincia = models.CharField(max_length=30, choices=provinciaSeleccion, default='buenos_aires')
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=50,default='')
    
    class Meta:
        ordering = ['nombre']
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
    
    def __str__(self):
        return self.nombre
