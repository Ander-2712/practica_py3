from django.shortcuts import render, redirect
from typing import Dict, Any
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def inicio_sesion(request):
    print(f'datos enviados por el metodo POST: {request.POST}')
    datos: Dict[str, Any] = {
        'titulo': 'Inicio de sesión',
        'empresa': 'Ferreteria C.A',
        'encabezado': 'Iniciar sesión',
        'estilo': 'd-flex align-items-center py-4',
    }
    
    if request.method == 'GET':
        return render(request, 'login/login.html', datos)
    else:
        usuario = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password'],                
        )