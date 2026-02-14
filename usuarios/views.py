from django.shortcuts import render
from typing import Dict, Any

# Create your views here.
def lista_usuarios(request):
    datos: Dict[str, Any] = {
        'titulo': 'Usuarios',
        'encabezado': 'Listado de usuarios',

    }
    return render(request, 'usuarios/listado.html', datos)