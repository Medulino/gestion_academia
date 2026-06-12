from django.db import models
from profesores.models import Profesor
from django.core.exceptions import ValidationError


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    profesor = models.ForeignKey(
        Profesor, on_delete=models.PROTECT, related_name="cursos"
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    plazas = models.PositiveIntegerField(default=20)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="cursos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        # 3. Lógica de validación
        if self.fecha_fin and self.fecha_inicio:
            if self.fecha_fin < self.fecha_inicio:
                raise ValidationError("La fecha final no puede ser anterior a la inicial.")


