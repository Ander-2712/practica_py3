from django.shortcuts import render
from typing import Dict, Any

# Create your views here.
def dasboard(request):
    datos: Dict[str, Any] = {
        'titulo': 'Página de inicio',
        'encabezado': 'Bienvenidos a la ferreteria',
    }
    
    return render(request, 'dashboard/index.html', datos)