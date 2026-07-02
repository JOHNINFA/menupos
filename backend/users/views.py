"""
Vistas de la app users. Ver mini-clase: docs/clases/07-jwt-autenticacion.md
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioSerializer


class MeView(APIView):
    """
    GET /api/users/me/  → datos del usuario actualmente logueado.

    Útil para que el frontend sepa, justo después del login, quién es
    el usuario y qué rol tiene (para mostrar u ocultar botones de admin).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UsuarioSerializer(request.user).data)
