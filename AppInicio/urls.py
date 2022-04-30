from django.urls import path
from .views import inicio, SobreNosotros

urlpatterns = [
   path('',inicio, name='Inicio'),
   path('about/',SobreNosotros, name='Sobre Nosotros'),  
]

   