from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('AppInicio.urls')),
    path('AppLogin/', include('AppLogin.urls')),
    path('admin/', admin.site.urls),
]