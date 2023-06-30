from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
   
        
class Mecanico(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    especialista= models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="mecanico", null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.rut

class Mantencion(models.Model):
    cod = models.CharField(max_length=10)
    descrip = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="mantencion", null=True)
    mecani = models.ForeignKey(Mecanico, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.id
    
tipos_contacto = [
    [0,"Sugerencia"],
    [1,"Reclamo"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=tipos_contacto)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre + " "+self.email
