from django import forms
from .models import RegistroCliente


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
