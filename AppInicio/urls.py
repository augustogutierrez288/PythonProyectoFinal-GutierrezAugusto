from django.urls import path
from .views import inicio, proyectos, blog

urlpatterns = [
   path('',inicio),
   path('proyectos/',proyectos, name='Proyectos'),
   path('blog',blog, name='Blog'),  
]

   