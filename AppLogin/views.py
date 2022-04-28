from .models import Avatar
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import NuestraCreacionUser, NuestraEdicionUser
from django.contrib.auth import login as django_login, authenticate


def IniciarSesion(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request,user)    
                return render(request, 'indice1/index.html', {'msj': 'Bienvenido a Everest:)','user_avatar_url':buscarAvatarUrl(request.user)})
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

@login_required
def EditarUser(request):
    msj = ''
    if request.method == 'POST':
        form = NuestraEdicionUser(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            request.user
            request.user.Email = data.get('Email')
            request.user.firstName = data.get('firstName','')
            request.user.lastName = data.get('lastName','')
            
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                request.user.set_password(data.get('password1')) 
            else:
                msj = 'No se Modifico la Contraseña'
            
            request.user.save()  
                     
            return render(request,'indice1/index.html', {'msj': msj, 'user_avatar_url':buscarAvatarUrl(request.user)})
        else:
            return render(request, 'indice2/editarUser.html', {'form': form, 'msj': '','user_avatar_url':buscarAvatarUrl(request.user)})
        
    form = NuestraEdicionUser(
        initial={
            'firstName': request.user.firstName, #profesor tengo un error en esta linea de codigo y no lo puedo solucionar.
            'lastName': request.user.lastName,
            'Email': request.user.Email,
            'userName': request.user.username
        } 
    )
    return render(request, 'indice2/editarUser.html', {'form': form, 'msj': '', 'user_avatar_url':buscarAvatarUrl(request.user)})  

def buscarAvatarUrl(user):
    return Avatar.objects.filter(user=user)[0].imagen.url