from django.db import models
from django.conf import settings
from django.contrib import admin

class Profesor(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profesor"
    )
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    biografia = models.TextField(blank=True)
    foto = models.ImageField(upload_to="profesores/", blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.first_name} " f"{self.usuario.last_name}"

