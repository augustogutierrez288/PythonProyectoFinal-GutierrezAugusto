from unicodedata import name
from django.urls import path
from .views import IniciarSesion

urlpatterns = [
    path('Iniciar Sesion/',IniciarSesion, name='Iniciar Sesion'),
]
