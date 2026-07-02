"""
Serializers del menú. Ver mini-clase: docs/clases/05-serializers.md
"""

from rest_framework import serializers
from .models import Categoria, Producto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']


class ProductoSerializer(serializers.ModelSerializer):
    # Campo extra de solo lectura: trae el nombre de la categoría además
    # de su ID, para que el frontend no tenga que hacer una petición aparte.
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'descripcion', 'precio',
            'categoria', 'categoria_nombre', 'imagen', 'disponible',
        ]
