# Migración de DATOS: convierte los estados viejos de las ventas ya
# existentes al nuevo flujo de 4 estados (FASE 6d).
#
# Antes: pendiente / pagada / cancelada
# Ahora: pedido / entregado / pagado / cancelado
#
# Una migración de datos (RunPython) es la forma profesional de no perder
# los registros existentes cuando cambia el significado de un campo.

from django.db import migrations


# Mapa de conversión: valor viejo -> valor nuevo
MAPA = {
    'pendiente': 'pedido',
    'pagada': 'pagado',
    'cancelada': 'cancelado',
}


def convertir_adelante(apps, schema_editor):
    Venta = apps.get_model('sales', 'Venta')
    for viejo, nuevo in MAPA.items():
        Venta.objects.filter(estado=viejo).update(estado=nuevo)


def convertir_atras(apps, schema_editor):
    # Permite revertir la migración (por si acaso): nuevo -> viejo.
    Venta = apps.get_model('sales', 'Venta')
    inverso = {nuevo: viejo for viejo, nuevo in MAPA.items()}
    for nuevo, viejo in inverso.items():
        Venta.objects.filter(estado=nuevo).update(estado=viejo)
    # 'entregado' no existía antes; lo mandamos a 'pendiente' si se revierte.
    Venta.objects.filter(estado='entregado').update(estado='pendiente')


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_venta_tipo_alter_venta_mesa'),
    ]

    operations = [
        migrations.RunPython(convertir_adelante, convertir_atras),
    ]
