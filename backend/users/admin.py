from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


# Extendemos UserAdmin (en vez de admin.ModelAdmin) para conservar toda
# la interfaz de gestión de contraseñas/permisos que Django ya trae,
# y solo le agregamos el campo `rol` a la lista visible.
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'rol', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('MenuPOS', {'fields': ('rol',)}),
    )


admin.site.register(Usuario, UsuarioAdmin)
