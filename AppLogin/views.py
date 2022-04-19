from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def IniciarSesion(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data('usuario')
            contraseña = form.cleaned_data('contraseña')
            
            user = authenticate(usuario=usuario, contraseña=contraseña)
            
            if user is not None:
                login(request,user)
                
                return render(request, 'indice1/index.html', {})
            else:
                return render(request, 'indice2/login.html', {'form': form, 'msj': 'Formulario Incorrecto'})
            
        else:
            return render(request, 'indice2/login.html', {'form': form, 'msj': 'Usuario Incorrecto'})
        
    form = AuthenticationForm()
    return render(request, 'indice2/login.html', {'form': form, 'msj': ''})