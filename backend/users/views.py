"""
Vistas de la app users. Ver mini-clase: docs/clases/07-jwt-autenticacion.md
"""

from django.db.models import ProtectedError
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Usuario
from .permissions import EsAdmin
from .serializers import UsuarioSerializer, UsuarioCreateSerializer


class MeView(APIView):
    """
    GET /api/users/me/  → datos del usuario actualmente logueado.

    Útil para que el frontend sepa, justo después del login, quién es
    el usuario y qué rol tiene (para mostrar u ocultar botones de admin).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UsuarioSerializer(request.user).data)


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Gestión de usuarios (meseros/admins). SOLO accesible para un admin
    (ver EsAdmin) — un mesero no puede ni siquiera LISTAR otros usuarios.
    """
    queryset = Usuario.objects.all().order_by('username')
    permission_classes = [EsAdmin]

    def get_serializer_class(self):
        # Al crear necesitamos el serializer con `password`.
        # Para listar/editar usamos el serializer "seguro" sin password.
        if self.action == 'create':
            return UsuarioCreateSerializer
        return UsuarioSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Sobreescribimos destroy() para dar un mensaje claro si se intenta
        borrar un mesero que YA tiene ventas registradas: el modelo Venta
        usa on_delete=PROTECT (ver sales/models.py) precisamente para
        evitar perder el historial, así que Django lanzaría un error feo
        de base de datos si no lo capturamos aquí.
        """
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {'error': 'No se puede borrar: este usuario tiene ventas registradas.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
