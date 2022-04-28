from django.db import models
from django.contrib.auth.models import User

#class estudiante(models.Model):
    #Nombre = models.CharField(max_length=20)
    #Apellido = models.CharField(max_length=30)
    #Email = models.EmailField
    
#class profesor(models.Model):
    #Nombre = models.CharField(max_length=20)
    #Apellido = models.CharField(max_length=30)
    #Email = models.EmailField
    #Profesion = models.CharField(max_length=30)
    
#class entregable(models.Model):
    #Nombre = models.CharField(max_length=20)
    #fechaDeEntrega = models.DateTimeField()
    #Entregado = models.BooleanField()
    
#class curso(models.Model):
    #Nombre = models.CharField(max_length=20)
    #camada = models.IntegerField()

class Avatar(models.Model):
    imagen = models.ImageField(upload_to = 'avatares',null= True, blank =True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)

 