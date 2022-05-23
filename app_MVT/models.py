from django.db import models

class Familia(models.Model):
    nombre=models.CharField(max_length=40)
    numero = models.IntegerField()
    fechaDeEntrega = models.DateField() 

