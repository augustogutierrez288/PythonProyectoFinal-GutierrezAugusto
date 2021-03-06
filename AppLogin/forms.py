from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuestraCreacionUser(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir Contraseña')
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k : '' for k in fields}

class NuestraEdicionUser(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    link = forms.URLField(required=False)
    more_description = forms.CharField(max_length=300,required=False)
    avatar = forms.ImageField(required=False)