from .models import UserExtension
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
                return render(request, 'indice1/index.html', {'msj': 'Bienvenido a Everest:)'})
            else:
                return render(request, 'accounts/login.html', {'form': form, 'msj': 'Formulario Incorrecto'})
            
        else:
            return render(request, 'accounts/login.html', {'form': form, 'msj': 'Usuario Incorrecto'})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form, 'msj': ''})  
   
def Registrar(request):
    if request.method == 'POST':
        form = NuestraCreacionUser(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request,'indice1/index.html', {'msj': f'Se Creo el usuario: {username}'})
        else:
            return render(request, 'accounts/Registrar.html', {'form': form, 'msj': ''})
        
    form = NuestraCreacionUser()
    return render(request, 'accounts/Registrar.html', {'form': form, 'msj': ''})

@login_required
def EditarUser(request):
    
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = NuestraEdicionUser(request.POST, request.FILES)
        
        if form.is_valid():
            
            request.user.email = form.cleaned_data['email']
            request.user.firstName = form.cleaned_data['firstName']
            request.user.lastName= form.cleaned_data['lastName']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.more_description = form.cleaned_data['more_description']
            
            if form.cleaned_data('password1') != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
                     
            return render(request,'indice1/index.html', {'msj': msj})
        else:
            return render(request, 'accounts/editarUser.html', {'form': form, 'msj': ''})
        
    form = NuestraEdicionUser(
        initial={
            'Email': request.user.email,
            'password1': '',
            'password2': '', 
            'firstName': request.user.firstName, #Hola Profesor no logro encontrar el error
            'lastName': request.user.lastName,
            'link':user_extension_logued.link,
            'more_description': user_extension_logued.more_description,
            'avatar':user_extension_logued.avatar,
        }
    )
    return render(request, 'accounts/editarUser.html', {'form': form, 'msj': ''})