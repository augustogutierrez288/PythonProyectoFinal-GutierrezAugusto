from django.contrib import admin

from AppLogin.models import curso, entregable, estudiante, profesor

# Register your models here.

admin.site.register(curso)
admin.site.register(profesor)
admin.site.register(entregable)
admin.site.register(estudiante)