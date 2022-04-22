from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request,'indice1/index.html', {})

def SobreNosotros(request):
    return HttpResponse('Blog')
