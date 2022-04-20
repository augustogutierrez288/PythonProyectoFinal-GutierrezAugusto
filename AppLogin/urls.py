from unicodedata import name
from django.urls import path
from .views import IniciarSesion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('Iniciar Sesion/',IniciarSesion, name= 'Iniciar Sesion'),
    path('Cerrar Sesion/',LogoutView.as_view(template_name='indice2/logaut.html'), name= 'Cerrar Sesion'),
]
