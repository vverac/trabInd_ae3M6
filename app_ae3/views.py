from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegistroClienteForm
from .models import RegistroCliente

# Create your views here.

class IndexView(TemplateView):
  template_name='app_ae3/landing.html'

def success(request):
 	#return HttpResponse('Bienvenido-Welcome')   
  return render(request, 'app_ae3/success.html') 


def formularioRegistroCliente(request):
  form = RegistroClienteForm()
  if request.method == 'POST':
      form = RegistroClienteForm(request.POST)
      if form.is_valid():
        registroCliente = RegistroCliente()
        registroCliente.nombre = form.cleaned_data['nombre']
        registroCliente.direccion = form.cleaned_data['direccion']
        registroCliente.email = form.cleaned_data['email']
        registroCliente.save()
      else:
        print('datos invalidos')  
      return redirect('/success')

  context={'form':form}
  return render(request, 'app_ae3/registroCliente.html', context = context) 
