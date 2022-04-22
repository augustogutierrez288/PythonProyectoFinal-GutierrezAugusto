from pyexpat import model
import django


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuestraCreacionUser(UserCreationForm):
    Email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir Contraseña')

    class Meta:
        model = User
        fields = ['username','Email','password1','password2']
        help_texts = {k : '' for k in fields}
        