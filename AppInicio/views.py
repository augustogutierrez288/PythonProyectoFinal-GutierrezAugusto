from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request,'indice1/index.html', {})

def blog(request):
    return HttpResponse('Blog')

def proyectos(request):
    return HttpResponse('Proyectos que nuestros Alumnos Crearon')
