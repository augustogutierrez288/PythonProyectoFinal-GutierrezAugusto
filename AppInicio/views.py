from django.shortcuts import render

def inicio(request):
    return render(request,'indice1/index.html', {})

def SobreNosotros(request):
    return render(request,'indice1/sobreNosotros.html', {})
       