from django import forms
from .models import RegistroCliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission


class RegistroClienteForm(forms.ModelForm):
  class Meta:
      model= RegistroCliente
      # fields = ['nombre','direccion','email']
      # es lo mismo estamos usando todos los datos
      fields = '__all__'

class LoginForm(forms.Form):
  # widget es para tener todas las validaciones
  nombre = forms.CharField(widget=forms.TextInput)
  password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm( UserCreationForm):
    email =  forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmacion contraseña', widget=forms.PasswordInput)
    date = forms.CharField()
    #haremos una metaclase que es para agregar informacion utilizada solo en ese tipo de dato
    # haremeos  agregaremos unos fields mas aca
    group= forms.ModelChoiceField(queryset=Group.objects.all())
    permissions=forms.ModelMultipleChoiceField(
    queryset=Permission.objects.all(),
    widget=forms.CheckboxSelectMultiple
)

    class Meta:
          model= User
          fields = ['username','email','password1','password2']
          help_texts= {k:'' for k in  fields }

