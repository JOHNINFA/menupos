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
        PENDIENTE = 'pendiente', 'Pendiente'
        PAGADA = 'pagada', 'Pagada'
        CANCELADA = 'cancelada', 'Cancelada'

    # settings.AUTH_USER_MODEL en vez de importar Usuario directamente:
    # es la forma recomendada por Django para referenciar el modelo de
    # usuario sin crear dependencias circulares entre apps.
    mesero = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,  # No se puede borrar un mesero con ventas registradas
        related_name='ventas',
    )

    fecha = models.DateTimeField(auto_now_add=True)

    # Se calcula sumando los subtotales de cada DetalleVenta (lo haremos
    # en la FASE 5 cuando conectemos esto a la API).
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )

    class Meta:
        ordering = ['-fecha']  # Las ventas más recientes primero

    def __str__(self):
        return f'Venta #{self.id} - {self.get_estado_display()} - ${self.total}'


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
