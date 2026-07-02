"""
Vistas de ventas. Ver mini-clase: docs/clases/06-viewsets-routers.md
"""

from rest_framework import viewsets, permissions
from .models import Venta
from .serializers import VentaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    # prefetch_related trae los detalles y sus productos en pocas
    # consultas extra (en vez de una consulta por cada detalle de cada venta).
    queryset = Venta.objects.select_related('mesero').prefetch_related('detalles__producto').all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]
