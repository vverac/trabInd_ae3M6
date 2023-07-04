from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegistroClienteForm, LoginForm,  UserRegistrationForm
from .models import RegistroCliente
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

class IndexView(TemplateView):
  template_name='app_ae3/landing.html'

def success(request):
 	#return HttpResponse('Bienvenido-Welcome')   
  return render(request, 'app_ae3/success.html') 

def home(request):
 	#return HttpResponse('Bienvenido-Welcome')   
  return render(request, 'app_ae3/home.html') 


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




# def login(request):
#   if request.method=='POST':
#       form=LoginForm(request.POST)
#       if form.is_valid():
#           usuario= form.cleaned_data["nombre"]
#           clave= form.cleaned_data["password"]
#           user = authenticate(request, username=usuario, password=clave)
#           # aca decimos si el usuario existe entonces hace el auth login
#           if user is not None:
#             if user.is_active:
#               auth_login(request, user)
#               # return HttpResponse('Autenticado correctamete')
#               return redirect('/home')
#             else:
#               return HttpResponse('Cuenta Deshabilitada')
#           else:
#             return HttpResponse("Login no valido")
#           # return render (request, 'aplicacion/home.html',{'user':user})
#           # si no es post el formulario va a estar vacio hasta que le demos render donde le damos el post
#   else:
#     form= LoginForm()
#     return render(request,'app_ae3/login.html',{'form':form})




@login_required
def register_user(request):
  # request es todo lo quee traemos de html
  # si quiero saber ssi se hizo un POST tengo que traer el request
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    #validamos el formulario
    if form.is_valid():
       # guardamos
      user = form.save()
      # una vez que tenemos el form guardado
      group=form.cleaned_data['group']
      permissions= form.cleaned_data['permissions']
      username= form.cleaned_data['username']
      # estoy entrando al atributo(group) del usuario y estoy agregando(add)) group
      user.groups.add(group)
      user.user_permissions.set(permissions)
      messages.success(request, f'Usuario {username} creado exitosamente')

      return redirect('/home')

  else:
    form = UserRegistrationForm()

  context={'form':form}
  return render(request, 'app_ae3/register_user.html', context = context) 