from django.contrib import admin
from .models import Curso
from django.utils.html import format_html


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    prepopulated_fields = {
    'slug': (
        'nombre',
    )
    }
    list_display = (
        "miniatura",
        "nombre",
        "profesor",
        "fecha_inicio",
        "fecha_fin",
        "activo",
    )
    search_fields = (
        "nombre",
        "descripcion",
        "profesor__usuario__first_name",
        "profesor__usuario__last_name",
    )
    list_filter = (
        "activo",
        "fecha_inicio",
    )
    ordering = ("nombre",)

    def miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="80"/>', obj.imagen.url)
        return "-"

    miniatura.short_description = "Imagen"



    fieldsets = (
        (
            "Información General",
            {
                "fields": (
                    "nombre",
                    "descripcion",
                    "profesor",
                    "slug",
                )
            },
        ),
        (
            "Planificación",
            {
                "fields": (
                    "fecha_inicio",
                    "fecha_fin",
                    "plazas",
                )
            },
        ),
        (
            "Publicación",
            {
                "fields": (
                    "activo",
                    "imagen",
                )
            },
        ),
    )
