from django import forms
from .models import RegistroCliente


class RegistroClienteForm(forms.ModelForm):
  class Meta:
      model= RegistroCliente
      # fields = ['nombre','direccion','email']
      # es lo mismo estamos usando todos los datos
      fields = '__all__'