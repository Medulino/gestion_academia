from django.contrib.auth.models import AbstractUser
from django.db import models



class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('alumno', 'Alumno'),
        ('profesor', 'Profesor'),
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO,
        default='alumno'
    )
    def __str__(self):
        return self.username