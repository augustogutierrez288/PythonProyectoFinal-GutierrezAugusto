from django.urls import path
from . import views

urlpatterns = [
   path('profesores/crear',views.profesoresCrear, name='profesoresCrear'),
   path('profesores/lista',views.profesoresList.as_view(), name='profesorList'),
   path("profesores/<int:pk>/editar/",views.profesoresEditar.as_view(), name= 'profesorEditar'),
   path("profesores/<int:pk>/borrar/",views.profesoresBorrar.as_view(), name= 'profesorBorrar'),
   path('estudiantes/lista',views.estudiantesList.as_view(), name='estudiantesList'),
   path("estudiantes/<int:pk>/editar/",views.estudiantesEditar.as_view(), name= 'estudiantesEditar'),
   path("estudiante/<int:pk>/borrar/",views.estudiantesBorrar.as_view(), name= 'estudiantesBorrar'),
   path('estudiantes/',views.estudiantesCrear, name='estudiantesCrear'),
   path('entregables/',views.entregables, name='entregables'),
   path('curso/',views.curso_formulario, name='curso_formulario'),
   path('formularios/',views.formularios,name='formularios'),
   path('buscador/',views.buscador,name='buscador'),
   path('buscadorCurso/',views.buscadorCurso,name='buscadorCurso'),
]
   