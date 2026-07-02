"""
Modelos del menú: Categoria y Producto.

Ver diagrama ER completo en: docs/clases/04-modelos-django.md
"""

from django.db import models


class Categoria(models.Model):
    """
    Agrupa productos (ej: "Hamburguesas", "Bebidas", "Postres").
    Analogía: una sección de la carta del restaurante.
    """
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        # Cómo se ve el nombre de este modelo en el Admin (plural correcto)
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']  # Orden alfabético por defecto

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """
    Un plato o bebida del menú. Pertenece a una Categoria.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    # DecimalField para dinero: nunca FloatField (ver clase 04, por qué).
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,  # Evita borrar una Categoría que tiene Productos
        related_name='productos',   # Permite hacer: categoria.productos.all()
    )

    # blank=True y null=True porque un producto puede no tener foto todavía.
    # upload_to='productos/' organiza las imágenes en media/productos/
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    disponible = models.BooleanField(
        default=True,
        help_text='Si está desactivado, no aparece en el POS para vender.'
    )

    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['categoria', 'nombre']

    def __str__(self):
        return self.nombre
