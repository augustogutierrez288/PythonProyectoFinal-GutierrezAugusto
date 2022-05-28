from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('AppInicio.urls')),
    path('AppLogin/', include('AppLogin.urls')),
    path('AppForm/', include('AppForm.urls')),
    path('admin/', admin.site.urls),
]

