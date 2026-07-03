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


class EsAdmin(BasePermission):
    """Exige rol='admin' para CUALQUIER acción, incluida la lectura."""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.rol == 'admin'
        )


class PuedeCrearVentaSoloAdminEdita(BasePermission):
    """
    Cualquier usuario autenticado (mesero o admin) puede LEER y CREAR ventas
    (tomar un pedido). Solo un admin puede EDITAR, BORRAR o cambiar el
    ESTADO (marcar_estado) de una venta.

    Analogía: cualquier mesero puede tomar el pedido, pero solo el cajero
    (admin) revisa y cierra la cuenta.

    Usamos `view.action` (no `request.method`) porque el ViewSet tiene una
    acción personalizada (`marcar_estado`) que también viaja por POST, y
    NO queremos que un método HTTP compartido abra una puerta trasera.

    `marcar_estado` está permitida para cualquier autenticado, pero la vista
    hace un chequeo extra: marcar 'pagado'/'cancelado' exige rol admin
    (marcar 'entregado' sí lo puede hacer el mesero). Ver sales/views.py.
    """

    ACCIONES_ABIERTAS = ('list', 'retrieve', 'create', 'marcar_estado')

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        if view.action in self.ACCIONES_ABIERTAS:
            return True
        return request.user.rol == 'admin'
