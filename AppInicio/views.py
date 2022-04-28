from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from AppLogin.views import buscarAvatarUrl

def inicio(request):
    return render(request,'indice1/index.html', {'user_avatar_url':buscarAvatarUrl(request.user)})

def SobreNosotros(request):
    return HttpResponse('Blog')
