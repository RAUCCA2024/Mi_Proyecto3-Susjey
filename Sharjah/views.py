from django.shortcuts import render, get_object_or_404
from .models import Propiedad, Agente, Cliente 

def listar_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'propiedades.html', {'propiedades': propiedades})

def detalle_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, pk=propiedad_id)
    return render(request, 'detalle_propiedad.html', {'propiedad': propiedad})

def listar_agentes(request):
    agentes = Agente.objects.all()
    return render(request, 'agentes.html', {'agentes': agentes})

def detalle_agente(request, agente_id):
    agente = get_object_or_404(Agente, pk=agente_id)
    return render(request, 'detalle_agente.html', {'agente': agente})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})