from django.urls import path
from . import views
# from django.views.generic import TemplateView
from app_ae3.views import IndexView

urlpatterns = [
   path('', IndexView.as_view())
]