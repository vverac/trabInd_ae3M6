from django.urls import path
from . import views
# from django.views.generic import TemplateView
from app_ae3.views import IndexView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', IndexView.as_view()),
   path('registroCliente/', views.formularioRegistroCliente, name='registroCliente'),
   path('success/', views.success, name='success'),
   # path('login/', views.login, name='login'),
   path('home/', views.home, name='home'),
   path('login/', LoginView.as_view(template_name='app_ae3/login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='app_ae3/logout.html'), name='logout'),
   path('register_user/', views.register_user, name='register_user'),
]