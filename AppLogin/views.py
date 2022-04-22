from django.shortcuts import render
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NuestraCreacionUser

def IniciarSesion(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request,user)    
                return render(request, 'indice1/index.html', {'msj': 'Bienvenido a Everest:)'})
            else:
                return render(request, 'indice2/login.html', {'form': form, 'msj': 'Formulario Incorrecto'})
            
        else:
            return render(request, 'indice2/login.html', {'form': form, 'msj': 'Usuario Incorrecto'})
    else:
        form = AuthenticationForm()
        return render(request, 'indice2/login.html', {'form': form, 'msj': ''})  
   
def Registrar(request):
    if request.method == 'POST':
        form = NuestraCreacionUser(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request,'indice1/index.html', {'msj': f'Se Creo el usuario: {username}'})
        else:
            return render(request, 'indice2/Registrar.html', {'form': form, 'msj': ''})
        
    form = NuestraCreacionUser()
    return render(request, 'indice2/Registrar.html', {'form': form, 'msj': ''})