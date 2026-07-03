"""
Modelos de ventas: Venta y DetalleVenta.

Ver diagrama ER completo en: docs/clases/04-modelos-django.md

Por qué 2 modelos separados:
- Venta      = la "factura completa" (quién, cuándo, total, estado)
- DetalleVenta = CADA línea de esa factura (ej: "2x Hamburguesa")
Una Venta puede tener VARIOS DetalleVenta (relación uno-a-muchos).
"""

from django.conf import settings
from django.db import models
from menu.models import Producto


class Venta(models.Model):
    """Una transacción completa: un pedido cobrado a un cliente."""

    class Estado(models.TextChoices):
        # Flujo real: el mesero toma el PEDIDO → lo lleva a la mesa y marca
        # ENTREGADO → el cajero marca PAGADO cuando el cliente paga.
        PEDIDO = 'pedido', 'Pedido'
        ENTREGADO = 'entregado', 'Entregado'
        PAGADO = 'pagado', 'Pagado'
        CANCELADO = 'cancelado', 'Cancelado'

    # Estados en los que una cuenta de mesa sigue "abierta" (el cliente
    # está en el local y aún no ha pagado): a esta cuenta se le pueden
    # sumar más productos. Ver create() en el serializer.
    ESTADOS_ABIERTOS = [Estado.PEDIDO, Estado.ENTREGADO]

    class Tipo(models.TextChoices):
        MESA = 'mesa', 'Mesa'
        LLEVAR = 'llevar', 'Para llevar'

    # settings.AUTH_USER_MODEL en vez de importar Usuario directamente:
    # es la forma recomendada por Django para referenciar el modelo de
    # usuario sin crear dependencias circulares entre apps.
    mesero = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,  # No se puede borrar un mesero con ventas registradas
        related_name='ventas',
    )

    fecha = models.DateTimeField(auto_now_add=True)

    tipo = models.CharField(
        max_length=10,
        choices=Tipo.choices,
        default=Tipo.MESA,
        help_text='Mesa (se atiende en el local) o Para llevar.',
    )

    # Número de mesa. null=True porque un pedido "Para llevar" NO tiene mesa.
    # Cuando tipo=mesa, el serializer valida que venga un número.
    mesa = models.PositiveIntegerField(
        null=True, blank=True, help_text='Número de mesa (solo si tipo=mesa).'
    )

    # Se calcula sumando los subtotales de cada DetalleVenta (ver
    # sales/serializers.py, VentaSerializer.create()).
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.PEDIDO,
    )

    class Meta:
        ordering = ['-fecha']  # Las ventas más recientes primero

    def __str__(self):
        ubicacion = f'Mesa {self.mesa}' if self.tipo == self.Tipo.MESA else 'Para llevar'
        return f'Venta #{self.id} - {ubicacion} - {self.get_estado_display()} - ${self.total}'


class DetalleVenta(models.Model):
    """Una línea dentro de una Venta: un producto y su cantidad."""

    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,  # Si se borra la Venta, se borran sus líneas
        related_name='detalles',
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,  # No se puede borrar un Producto ya vendido
        related_name='detalles_venta',
    )
    cantidad = models.PositiveIntegerField(default=1)

    # "Fotografiamos" el precio al momento de la venta. Si mañana el
    # producto sube de precio, esta venta histórica NO debe cambiar.
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def subtotal(self):
        # @property = se calcula al vuelo, NO se guarda en la base de datos.
        # Evita datos duplicados/desincronizados (cantidad * precio siempre fresco).
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f'{self.cantidad}x {self.producto.nombre}'
