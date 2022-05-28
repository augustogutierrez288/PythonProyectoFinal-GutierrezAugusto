from django.contrib import admin
from .models import Estudiantes, Profesor, Entregable, Curso

admin.site.register(Estudiantes)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Curso)
