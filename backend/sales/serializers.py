"""
Serializers de ventas. Ver mini-clase: docs/clases/05-serializers.md
"""

from rest_framework import serializers
from .models import Venta, DetalleVenta


class DetalleVentaSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()  # usa la @property del modelo
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetalleVenta
        fields = ['id', 'producto', 'producto_nombre', 'cantidad', 'precio_unitario', 'subtotal']
        # precio_unitario NO lo manda el frontend: lo calculamos nosotros
        # en el create() de VentaSerializer, tomando el precio actual del
        # producto (evita que el cliente "invente" un precio distinto).
        read_only_fields = ['precio_unitario']


class VentaSerializer(serializers.ModelSerializer):
    # many=True porque una Venta trae UNA LISTA de detalles anidados.
    detalles = DetalleVentaSerializer(many=True)
    mesero_nombre = serializers.CharField(source='mesero.username', read_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'mesero', 'mesero_nombre', 'fecha', 'total', 'estado', 'detalles']
        # El mesero se asigna automáticamente desde request.user (ver create),
        # y el total se calcula solo — el frontend nunca los envía directamente.
        read_only_fields = ['mesero', 'total', 'fecha']

    def create(self, validated_data):
        """
        Sobreescribimos create() porque una Venta no es un registro simple:
        hay que crear la Venta Y todos sus DetalleVenta juntos, y calcular
        el total sumando cada línea (usando el precio ACTUAL del producto,
        no uno que el cliente podría intentar manipular).
        """
        detalles_data = validated_data.pop('detalles')
        mesero = self.context['request'].user

        venta = Venta.objects.create(mesero=mesero, **validated_data)

        total = 0
        for detalle in detalles_data:
            producto = detalle['producto']
            cantidad = detalle['cantidad']
            precio_unitario = producto.precio  # "fotografía" del precio actual

            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
            )
            total += cantidad * precio_unitario

        venta.total = total
        venta.save()
        return venta
