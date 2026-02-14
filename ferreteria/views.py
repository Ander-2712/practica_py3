from django.shortcuts import render
from typing import Dict, Any

def inicio(request):
    datos: Dict[str, Any] = {
        'titulo': 'Página de inicio',
        'encabezado': 'Bienvenidos a la ferreteria',
    }
    
    return render(request, 'ferreteria/index.html', datos)