from django.shortcuts import render
from django.urls import reverse_lazy
from AppForm.models import Curso, Profesor, Estudiantes,Entregable
from AppForm.forms import CursoFormulario,ProfesorFormulario,EstudiantesFormulario,EntregableFormulario, BuscadorCursoFormulario
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
def formularios(request):
    return render(request,'indice2/formularios.html', {})

def profesoresCrear(request):
    if request.method =='POST':
        
        formulario_profesor = ProfesorFormulario(request.POST)
        print(formulario_profesor)
        
        if formulario_profesor.is_valid:
            data = formulario_profesor.cleaned_data
            profesor = Profesor (nombre = data['nombre'], apellido = data['apellido'], email = data['email'], profesor = data['profesor'])
            profesor.save()
            return render(request,'indice1/index.html',{'msj':f'Se Creo Exitosamente el profesor: {profesor}'}) 
    else:
        formulario_profesor = ProfesorFormulario    
            
    return render(request,'indice2/profesores.html',{"formulario_profesor": formulario_profesor})

class profesoresList(ListView):
    model = Profesor
    template_name = 'indice2/leerProfesor.html'

class profesoresEditar(UpdateView):
    model = Profesor
    template_name = 'AppForm/profesor_form.html'
    success_url = "/AppForm/profesores/lista"
    fields = ['nombre','apellido','email','profesor']

class profesoresBorrar(DeleteView):
    model = Profesor
    template_name = 'AppForm/profesor_confirm_delete.html'
    success_url = "/AppForm/profesores/lista"
    
def estudiantesCrear(request):
    if request.method =='POST':
        
        formulario_estudiante = ProfesorFormulario(request.POST)
        print(formulario_estudiante)
        
        if formulario_estudiante.is_valid:
            data = formulario_estudiante.cleaned_data
            estudiante = Estudiantes (nombre = data['nombre'], apellido = data['apellido'], email = data['email'])
            estudiante.save()
            return render(request,'indice1/index.html',{'msj':f'Se Creo Exitosamente el estudiante: {estudiante}'}) 
    else:
        formulario_estudiante = EstudiantesFormulario   
            
    return render(request,'indice2/estudiantes.html',{"formulario_estudiante": formulario_estudiante})
    
class estudiantesList(ListView):
    model= Estudiantes
    template_name= 'indice2/leerEstudiante.html'

class estudiantesEditar(UpdateView):
    model = Estudiantes
    template_name = 'AppForm/estudiantes_form.html'
    success_url = "/AppForm/estudiantes/lista"
    fields = ['nombre','apellido','email']

class estudiantesBorrar(DeleteView):
    model = Estudiantes
    template_name = 'AppForm/profesor_confirm_delete.html'
    success_url = "/AppForm/estudiantes/lista"

def entregables(request):
    if request.method =='POST':
        
        formulario_entregables = EntregableFormulario(request.POST)
        print(formulario_entregables)
        
        if formulario_entregables.is_valid:
            data = formulario_entregables.cleaned_data
            entregables = Entregable (nombre = data['nombre'], fechaDeEntrega = data['fechaDeEntrega'], entregable = data['entregable'])
            entregables.save()
            return render(request,'indice1/index.html',{'msj':f'Se entrego Exitosamente: {entregables}'}) 
    else:
        formulario_entregables = EntregableFormulario 
            
    return render(request,'indice2/entregables.html',{"formulario_entregables": formulario_entregables})
    

def curso_formulario(request):
    if request.method =='POST':
        formulario = CursoFormulario(request.POST)
        
        print(formulario)
        
        if formulario.is_valid:
            data = formulario.cleaned_data
            nuevo_curso = Curso (nombre = data['curso'], camada = data['camada'])
            nuevo_curso.save()
            return render(request,'indice1/index.html',{'msj':f'Se Creo Exitosamente: {nuevo_curso}'}) 
    else:
        formulario = CursoFormulario        
    return render(request,'indice2/formularioCurso.html',{"formulario": formulario})

def buscador(request):
    return render(request,'indice2/buscador.html',{})

def buscadorCurso(request):
    cursos_buscados = []
    dato = request.GET.get('curso',None)
   
    if dato is not None:
        cursos_buscados = Curso.objects.filter(nombre__icontains=dato)
    
    buscador = BuscadorCursoFormulario
    return render(
        request,'indice2/buscarCurso.html',{'buscador':buscador, 'cursos_buscados' : cursos_buscados, 'dato':dato}
    )
    
    
       
