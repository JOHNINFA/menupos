"""
Permisos personalizados de MenuPOS.

Ver mini-clase: docs/clases/06-viewsets-routers.md
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class EsAdminOSoloLectura(BasePermission):
    """
    Cualquier usuario autenticado puede LEER (GET, HEAD, OPTIONS).
    Solo un usuario con rol='admin' puede ESCRIBIR (POST, PUT, PATCH, DELETE).

    Analogía: cualquier mesero puede mirar el menú, pero solo el
    administrador (chef) puede cambiar las recetas.
    """

    def has_permission(self, request, view):
        # SIEMPRE exigimos estar logueado, sea para leer o escribir.
        # Sin esta línea, cualquiera sin token podría leer el menú completo.
        if not (request.user and request.user.is_authenticated):
            return False

        if request.method in SAFE_METHODS:
            return True
        return request.user.rol == 'admin'
