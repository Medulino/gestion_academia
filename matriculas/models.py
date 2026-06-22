from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from cursos.models import Curso
class Matricula(models.Model):
    alumno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    fecha_matricula = models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        unique_together = (
            'alumno',
            'curso'
        )
    def __str__(self):
        return (
            f"{self.alumno.username}"
            f" - "
            f"{self.curso.nombre}"
        )