from django.db import models

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    profesor = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email} {self.profesor}'
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateTimeField()
    entregable = models.BooleanField()
    
    def __str__(self):
            return f'{self.nombre}'
        
class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()
    
    def __str__(self):
        return f'Curso: {self.nombre} - Camada: {self.camada}'
        