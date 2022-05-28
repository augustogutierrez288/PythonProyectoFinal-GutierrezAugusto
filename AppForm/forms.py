from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    profesor = forms.CharField(max_length=20)
    
class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    fechaDeEntrega = forms.DateTimeField()
    entregable = forms.BooleanField()

class BuscadorCursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)