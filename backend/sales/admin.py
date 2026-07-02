from django.contrib import admin
from .models import Venta, DetalleVenta


class DetalleVentaInline(admin.TabularInline):
    # Inline = permite editar los DetalleVenta DENTRO de la pantalla de Venta,
    # en vez de tener que ir a otra sección del Admin.
    model = DetalleVenta
    extra = 0  # No mostrar filas vacías extra por defecto


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesero', 'fecha', 'total', 'estado')
    list_filter = ('estado', 'fecha')
    inlines = [DetalleVentaInline]
