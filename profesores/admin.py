from django.contrib import admin
from profesores.models import Profesor
from django.utils.html import format_html
@admin.register(Profesor)

class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        "miniatura",
        "usuario",
        "especialidad",
        "telefono",
    )
    search_fields = (
        "usuario__username",
        "usuario__first_name",
        "usuario__last_name",
        "especialidad",
    )


    list_filter = ("especialidad",)

    ordering = ("usuario__last_name",)


    def miniatura(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="50"/>', obj.foto.url)
        return "-"

    miniatura.short_description = "Foto"
