"""
Vistas del menú. Ver mini-clase: docs/clases/06-viewsets-routers.md
"""

from rest_framework import viewsets
from users.permissions import EsAdminOSoloLectura
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [EsAdminOSoloLectura]


class ProductoViewSet(viewsets.ModelViewSet):
    # select_related trae la Categoria en la MISMA consulta SQL
    # (evita hacer 1 consulta extra por cada producto - más eficiente).
    queryset = Producto.objects.select_related('categoria').all()
    serializer_class = ProductoSerializer
    permission_classes = [EsAdminOSoloLectura]
