"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
#Para importar las vistas de la aplicación catalogo_libros
from catalogo_libros import views

urlpatterns = [
   path('admin/', admin.site.urls),
   ##Para mostrar el index de libros de manera predeterminada
   path('', views.index, name='index'),
    path('catalogo_libros/', include('catalogo_libros.urls')),
    path('/', RedirectView.as_view(url='catalogo_libros/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
