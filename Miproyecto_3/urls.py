"""
URL configuration for Miproyecto_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from Sharjah import views 

urlpatterns = [
    path('admin/', admin.site.urls),  # URL de administrador
    path('propiedades/', views.listar_propiedades, name='listar_propiedades'),
    path('propiedades/<int:propiedad_id>/', views.detalle_propiedad, name='detalle_propiedad'),
    path('agentes/', views.listar_agentes, name='listar_agentes'),
    path('agentes/<int:agente_id>/', views.detalle_agente, name='detalle_agente'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
]

