from django.db import models

# Create your models here.

## CLASE 24 #####################################################################
from django.contrib.auth.models import User

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
#################################################################################



class Pais(models.Model):
        nombre = models.CharField(max_length=100)

        def __str__(self):
                return self.nombre
                
class Tipo_inmueble(models.Model):
        nombre = models.CharField(max_length=80, unique=True)

        def __str__(self):
                return self.nombre

class Arrendador(models.Model):
        dni = models.CharField(max_length=12) 
        nombre = models.CharField(max_length=30)
        apellido = models.CharField(max_length=30)
        email = models.EmailField()
        domicilio = models.CharField(max_length=50)


        def __str__(self):
                return f"{self.nombre} {self.apellido}"

class Arrendatario(models.Model):
        dni = models.CharField(max_length=12)
        nombre = models.CharField(max_length=30)
        apellido = models.CharField(max_length=30)
        email = models.EmailField()
        domicilio = models.CharField(max_length=50)
  

        def __str__(self):
              return f"{self.nombre} {self.apellido}"

class Inmueble(models.Model):
        nombre = models.CharField(max_length=12)
        medidas = models.CharField(max_length=20)
        precio = models.CharField(max_length=10)
        direccion = models.CharField(max_length=50)
        tipo = models.ForeignKey(Tipo_inmueble, on_delete=models.SET_NULL, null=True, blank=True)

        def __str__(self):
              return f"{self.nombre}"
        
