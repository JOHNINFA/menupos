# 📖 Clase 06 — ViewSets y Routers (el comedor)

> 🎯 **Objetivo**: Entender cómo DRF conecta URLs con la lógica que responde cada petición.
> ⏱️ **Tiempo**: 7 minutos
> 📚 **Pre-requisitos**: Clase [`05-serializers.md`](05-serializers.md)

---

## 🤔 El problema

Para cada modelo necesitamos 5 acciones básicas: listar, ver uno, crear, editar, borrar. Escribir una función por cada una = mucho código repetido.

## 🍽️ La solución: ViewSet

Un **ViewSet** agrupa TODAS esas acciones en una sola clase:

```python
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()      # ¿de dónde saca los datos?
    serializer_class = ProductoSerializer  # ¿cómo los traduce a JSON?
```

Con SOLO estas 3 líneas, `ModelViewSet` te da automáticamente:

| Verbo + URL | Acción |
|---|---|
| `GET /productos/` | Listar todos |
| `POST /productos/` | Crear uno nuevo |
| `GET /productos/5/` | Ver el producto 5 |
| `PUT /productos/5/` | Reemplazar el producto 5 |
| `PATCH /productos/5/` | Editar parcialmente el producto 5 |
| `DELETE /productos/5/` | Borrar el producto 5 |

## 🎬 Analogía

El ViewSet es el **comedor** del restaurante: sin importar si el cliente quiere ver el menú, pedir algo nuevo, cambiar su pedido o cancelarlo, todo pasa por el mismo "mostrador" (la clase), que sabe manejar cada caso.

---

## 🚪 Router — la puerta automática

En vez de escribir manualmente cada URL, el **Router** las genera solas:

```python
from rest_framework.routers import DefaultRouter
from menu.views import ProductoViewSet, CategoriaViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('categorias', CategoriaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

Esto genera automáticamente TODAS las URLs de la tabla de arriba, para `productos` Y `categorias`, sin escribirlas a mano.

## 🎬 Analogía
El Router es como **poner un letrero automático en la puerta**: "Sección Productos → aquí", "Sección Categorías → allá", sin que el arquitecto tenga que dibujar cada puerta individualmente.

---

## 🔐 Permisos: ¿quién puede hacer qué?

No todos deben poder editar el menú. Creamos un permiso personalizado:

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS

class EsAdminOSoloLectura(BasePermission):
    """Cualquiera autenticado puede LEER. Solo un admin puede ESCRIBIR."""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user.is_authenticated and request.user.rol == 'admin'
```

Y se lo asignamos al ViewSet:

```python
class ProductoViewSet(viewsets.ModelViewSet):
    ...
    permission_classes = [EsAdminOSoloLectura]
```

### Analogía
Es como un **guardia en la puerta de la cocina**: cualquier mesero puede mirar el menú, pero solo el administrador (chef) puede cambiar las recetas.

---

## 🧠 Quiz rápido

1. ¿Qué acciones te da gratis un `ModelViewSet`?
2. ¿Para qué sirve un Router?
3. ¿Qué hace `SAFE_METHODS`?
4. ¿Por qué creamos un permiso personalizado en vez de usar solo `IsAuthenticated`?

> 📝 Respuestas en el quiz de FASE 5.

## 🔗 Referencias
- [DRF ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)
- [DRF Routers](https://www.django-rest-framework.org/api-guide/routers/)
- [DRF Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
