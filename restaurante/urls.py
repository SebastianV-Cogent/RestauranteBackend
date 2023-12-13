"""
URL configuration for restaurante project.

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
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
        #Rutas para el usuario
    path('usuarios/crearUsuario', views.crearUsuario),
    path('usuarios/obtenerUsuario', views.obtenerUsuario),
    path('usuarios/actualizarUsuario', views.actualizarUsuario),
        #Rutas para la sucursal
    path('sucursal/crearSucursal', views.crearSucursal),
    path('sucursal/obtenerSucursal', views.obtenerSucursal),
    path('sucursal/obtenerTodasLasSucursales', views.obtenerTodasLasSucursales),
        #Rutas para intolerancias
    path('intolerancias/crearIntolerancia', views.crearIntolerancias),
    path('intolerancias/obtenerIntolerancias', views.obtenerIntolerancias),
    path('intolerancias/crearListaIntolerancias', views.crearListaIntolerancias),
        #Rutas para ingredientes
    path('ingredientes/crearIngrediente', views.crearIngredientes),
    path('ingredientes/obtenerIngredientes', views.obtenerIngredientes),
    path('ingredientes/crearListaIngredientes', views.crearListaIngredientes),
        #Rutas para necesidades
    path('necesidades/crearNecesidad', views.crearNecesidades),
    path('necesidades/obtenerNecesidades', views.obtenerNecesidades),
    path('necesidades/crearListaNecesidades', views.crearListaNecesidades),
        #Rutas para preferencias
    path('preferencias/crearPreferencia', views.crearPreferencias),
    path('preferencias/obtenerPreferencias', views.obtenerPreferencias),
    path('preferencias/crearListaPreferencias', views.crearListaPreferencias),
        #Rutas para enfermedades
    path('enfermedades/crearEnfermedad', views.crearEnfermedad),
    path('enfermedades/obtenerEnfermedades', views.obtenerEnfermedades),
    path('enfermedades/crearListaEnfermedades', views.crearListaEnfermedades),
    path('enfermedades/crearListaAlergias', views.crearListaAlergias),
        #Rutas para pedidos
    path('pedidos/crearPedido', views.crearPedido),
    path('pedidos/crearListaPedidos', views.crearListaPedidos),
        #Rutas para pedidos
    path('recomendaciones/obtenerPlatillosRecomendados', views.obtenerPlatillosRecomendados),
]
