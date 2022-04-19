from django.db import models

class estudiante(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=30)
    Email = models.EmailField
    
class profesor(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=30)
    Email = models.EmailField
    Profesion = models.CharField(max_length=30)
    
class entregable(models.Model):
    Nombre = models.CharField(max_length=20)
    fechaDeEntrega = models.DateTimeField()
    Entregado = models.BooleanField()
    
class curso(models.Model):
    Nombre = models.CharField(max_length=20)
    camada = models.IntegerField()



 