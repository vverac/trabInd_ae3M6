from django.db import models

# Create your models here.
# from django.conf import settings

# from django.utils import timezone


class Cliente(models.Model):
  # def __init__(self, nombre, edad):
      nombre = models.CharField(max_length=200)
      edad = models.CharField(max_length=200)

      def __str__(self):
        return self.nombre
