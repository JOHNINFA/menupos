"""
Vistas de ventas. Ver mini-clase: docs/clases/06-viewsets-routers.md
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from users.permissions import PuedeCrearVentaSoloAdminEdita
from .models import Venta
from .serializers import VentaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    # prefetch_related trae los detalles y sus productos en pocas
    # consultas extra (en vez de una consulta por cada detalle de cada venta).
    queryset = Venta.objects.select_related('mesero').prefetch_related('detalles__producto').all()
    serializer_class = VentaSerializer

    # Cualquier autenticado lee y crea (tomar el pedido). Solo admin puede
    # editar/borrar directamente — pero además `estado` es de solo lectura
    # en el serializer, así que la ÚNICA forma de cambiarlo es esta acción.
    permission_classes = [PuedeCrearVentaSoloAdminEdita]

    # Marcar PAGADO o CANCELADO afecta el dinero → solo el cajero/admin.
    # Marcar ENTREGADO lo puede hacer el mesero (él lleva los platos).
    ESTADOS_SOLO_ADMIN = (Venta.Estado.PAGADO, Venta.Estado.CANCELADO)

    @action(detail=True, methods=['post'])
    def marcar_estado(self, request, pk=None):
        """
        POST /api/ventas/{id}/marcar_estado/  {"estado": "entregado"}

        Endpoint dedicado para avanzar el estado de una venta. Separarlo de
        un PATCH genérico evita que alguien intente colar cambios en
        mesero/total/detalles junto con el estado — aquí SOLO se toca estado.

        Permisos:
        - 'entregado': cualquier usuario autenticado (el mesero que sirve).
        - 'pagado'/'cancelado': solo admin (decisiones de caja).
        """
        venta = self.get_object()
        nuevo_estado = request.data.get('estado')

        if nuevo_estado not in Venta.Estado.values:
            return Response(
                {'error': f'Estado inválido. Usa uno de: {Venta.Estado.values}'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if nuevo_estado in self.ESTADOS_SOLO_ADMIN and request.user.rol != 'admin':
            return Response(
                {'error': 'Solo un administrador puede marcar pagado o cancelado.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        venta.estado = nuevo_estado
        venta.save()
        return Response(VentaSerializer(venta).data)
