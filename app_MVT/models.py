from django.db import models

class Futbol(models.Model):
    numeroDeSocio = models.IntegerField()
    nombre=models.CharField(max_length=40)
    fechaDeIngreso = models.DateField() 
    email = models.EmailField()

class Tenis(models.Model):
    numeroDeSocio = models.IntegerField()
    nombre=models.CharField(max_length=40)
    fechaDeIngreso = models.DateField() 
    email = models.EmailField()

class Basquet(models.Model):
    numeroDeSocio = models.IntegerField()
    nombre=models.CharField(max_length=40)
    fechaDeIngreso = models.DateField() 
    email = models.EmailField()

    
