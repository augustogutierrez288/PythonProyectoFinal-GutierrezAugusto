from django.urls import path
from .views import IniciarSesion, Registrar, EditarUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('Iniciar Sesion/',IniciarSesion, name= 'Iniciar Sesion'),
    path('Cerrar Sesion/',LogoutView.as_view(template_name='accounts/logaut.html'), name= 'Cerrar Sesion'),
    path('Registrar/',Registrar, name='Registrar'),
    path('Editar/',EditarUser, name='Editar Usuario'),
]