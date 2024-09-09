from django.db import models

# Create your models here.

class Amp(models.Model):
    nombre= models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='amp/', blank=True, null=True)
    

    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo: {self.tipo} - Modelo {self.modelo} " 


class Pedal(models.Model):
    nombre= models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='pedal/', blank=True, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo: {self.tipo} - Modelo {self.modelo} " 

class Portapuas(models.Model):
    nombre= models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='porta/', blank=True, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo: {self.tipo} - Modelo {self.modelo} " 

class Instrumento(models.Model):
    nombre= models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='inst/', blank=True, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo: {self.tipo} - Modelo {self.modelo} " 
