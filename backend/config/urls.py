"""
URLs raíz de MenuPOS.

Ver mini-clases:
- docs/clases/06-viewsets-routers.md (Router)
- docs/clases/07-jwt-autenticacion.md (login/refresh)
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from menu.views import CategoriaViewSet, ProductoViewSet
from sales.views import VentaViewSet
from users.views import MeView, UsuarioViewSet

# El Router genera automáticamente las 6 rutas típicas (GET/POST/PUT/PATCH/DELETE)
# para cada ViewSet registrado. Ver clase 06 para el detalle completo.
router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('productos', ProductoViewSet)
router.register('ventas', VentaViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Todas las rutas del Router quedan bajo /api/
    # (ej: /api/productos/, /api/ventas/5/)
    path('api/', include(router.urls)),

    # Autenticación JWT: la "recepción" donde se entrega la pulsera VIP
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Info del usuario logueado (para que el frontend sepa su rol)
    path('api/users/me/', MeView.as_view(), name='me'),
]

# Solo en desarrollo (DEBUG=True): Django sirve las imágenes subidas
# (media/) directamente. En producción esto lo hará AWS S3 (FASE 7).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
