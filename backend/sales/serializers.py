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
        fields = ['id', 'mesero', 'mesero_nombre', 'fecha', 'tipo', 'mesa', 'total', 'estado', 'detalles']
        # El mesero se asigna automáticamente desde request.user (ver create),
        # y el total se calcula solo — el frontend nunca los envía directamente.
        # `tipo` y `mesa` los manda el frontend al crear. `estado` es de solo
        # lectura aquí a propósito: se cambia con el endpoint dedicado
        # /marcar_estado/ (ver VentaViewSet), no reescribiendo la venta.
        read_only_fields = ['mesero', 'total', 'fecha', 'estado']

    def validate(self, data):
        # Un pedido de mesa DEBE tener número de mesa. Uno "para llevar" no.
        if data.get('tipo') == Venta.Tipo.MESA and not data.get('mesa'):
            raise serializers.ValidationError({'mesa': 'Indica el número de mesa.'})
        return data

    def create(self, validated_data):
        """
        Sobreescribimos create() porque una Venta no es un registro simple:
        hay que crear la Venta Y sus DetalleVenta, y calcular el total
        sumando cada línea (con el precio ACTUAL del producto, no uno que
        el cliente podría manipular).

        Reglas de negocio (FASE 6c/6d):

        1. La venta nace en estado 'pedido': el mesero la toma; luego la
           entrega (ENTREGADO) y el cajero la cobra (PAGADO).

        2. Cuenta abierta por mesa: si es un pedido de MESA y esa mesa YA
           tiene una cuenta abierta (estado pedido o entregado), sumamos los
           nuevos productos a esa cuenta en vez de crear otra (ej: la mesa
           pide otra gaseosa). Al agregar productos nuevos, la cuenta vuelve
           a 'pedido' porque hay algo nuevo que preparar/entregar.
           Los pedidos "para llevar" siempre son independientes.
        """
        detalles_data = validated_data.pop('detalles')
        mesero = self.context['request'].user
        tipo = validated_data.get('tipo', Venta.Tipo.MESA)
        mesa = validated_data.get('mesa')

        venta = None
        if tipo == Venta.Tipo.MESA and mesa is not None:
            # ¿Ya hay una cuenta abierta (sin pagar) para esta mesa?
            venta = Venta.objects.filter(
                tipo=Venta.Tipo.MESA,
                mesa=mesa,
                estado__in=Venta.ESTADOS_ABIERTOS,
            ).first()

        if venta is None:
            venta = Venta.objects.create(
                mesero=mesero, estado=Venta.Estado.PEDIDO, **validated_data
            )

        # Partimos del total que ya tuviera la cuenta (0 si es nueva) y
        # le sumamos los productos de esta ronda.
        total = venta.total
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
        # Hay productos nuevos por preparar/entregar → vuelve a 'pedido'.
        venta.estado = Venta.Estado.PEDIDO
        venta.save()
        return venta
