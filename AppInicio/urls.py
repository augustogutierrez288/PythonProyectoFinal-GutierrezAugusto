from django.urls import path
from .views import inicio, SobreNosotros

urlpatterns = [
   path('',inicio, name='Inicio'),
   path('Sobre Nosotros',SobreNosotros, name='Sobre Nosotros'),  
]

   