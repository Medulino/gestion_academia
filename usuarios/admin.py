from django.contrib import admin
from .models import Usuario
admin.site.register(Usuario)
from django.contrib.auth.admin import UserAdmin # 1. Importar UserAdmin
# 2. Crear una clase que herede de UserAdmin
class UsuarioAdmin(UserAdmin):
    # Como agregaste el campo 'tipo', debes incluirlo en los fieldsets
    # para que aparezca en el formulario del admin.
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('tipo',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('tipo',)}),
    )
    
    list_display = ('username', 'email', 'tipo', 'is_staff', 'is_active')
