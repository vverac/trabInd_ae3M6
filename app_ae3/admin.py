from django.contrib import admin
from .models import Cliente, RegistroCliente
from django.contrib.auth.decorators import login_required

# Register your models here.

admin.site.register(Cliente)
admin.site.register(RegistroCliente)
admin.site.login = login_required(admin.site.login)