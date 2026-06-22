from django.contrib import admin
from django.contrib import admin
from datetime import timedelta
from django.contrib import admin
from django.utils import timezone


class FiltroFechas(admin.SimpleListFilter):
    title = "Fecha inicio"
    parameter_name = "periodo"

    def lookups(self, request, model_admin):
        return (
            ("hoy", "Hoy"),
            ("manana", "Mañana"),
            ("semana", "Esta semana"),
            ("mes", "Este mes"),
            ("anio", "Este año"),
        )

    def queryset(self, request, queryset):
        now = timezone.now()
        hoy = now.date()

        if self.value() == "hoy":
            return queryset.filter(fecha_inicio=hoy)

        if self.value() == "manana":
            manana = hoy + timedelta(days=1)
            return queryset.filter(fecha_inicio=manana)

        if self.value() == "semana":
            inicio = hoy - timedelta(days=hoy.weekday())
            fin = inicio + timedelta(days=7)
            return queryset.filter(fecha_inicio__gte=inicio, fecha_inicio__lt=fin)

        if self.value() == "mes":
            inicio = hoy.replace(day=1)
            if hoy.month == 12:
                fin = hoy.replace(year=hoy.year + 1, month=1, day=1)
            else:
                fin = hoy.replace(month=hoy.month + 1, day=1)
            return queryset.filter(fecha_inicio__gte=inicio, fecha_inicio__lt=fin)

        if self.value() == "anio":
            inicio = hoy.replace(month=1, day=1)
            fin = hoy.replace(year=hoy.year + 1, month=1, day=1)
            return queryset.filter(fecha_inicio__gte=inicio, fecha_inicio__lt=fin)

        return queryset
