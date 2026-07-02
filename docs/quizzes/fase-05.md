# 🧠 Quiz FASE 5 — API REST completa (Serializers, ViewSets, JWT)

> 📚 **Clases que cubre**: [`05-serializers.md`](../clases/05-serializers.md), [`06-viewsets-routers.md`](../clases/06-viewsets-routers.md), [`07-jwt-autenticacion.md`](../clases/07-jwt-autenticacion.md)

---

## 📝 Preguntas

1. ¿Qué hace un Serializer, en una frase?
2. ¿Para qué sirve `source='categoria.nombre'` en un serializer?
3. ¿Por qué sobreescribimos `create()` en `VentaSerializer` en vez de dejar el comportamiento por defecto?
4. ¿Qué acciones te da gratis un `ModelViewSet`?
5. ¿Para qué sirve un Router?
6. ¿Qué bug encontramos en `EsAdminOSoloLectura` al probarlo, y cómo lo arreglamos?
7. ¿Cuál es la diferencia entre access token y refresh token?
8. ¿Por qué el `precio_unitario` de un `DetalleVenta` se toma del producto en el servidor, y NO se acepta desde el frontend?
9. ¿Qué código HTTP recibe un mesero al intentar crear un Producto, y por qué?
10. ¿Qué hace `select_related` / `prefetch_related` y por qué los usamos en los ViewSets?

---

---

---

## ✅ Respuestas

<br><br><br>

### 1. Traduce entre objetos Python (modelos) y JSON, en ambas direcciones, validando los datos en el proceso.

### 2. Permite mostrar un campo de un objeto **relacionado** (la Categoría del Producto) sin exponer el objeto completo — solo el dato puntual que necesitamos (su nombre).

### 3. Porque crear una Venta implica una lógica especial: crear varios `DetalleVenta` a la vez y **calcular el total** sumando cada línea. El comportamiento por defecto de DRF no sabe hacer eso automáticamente para relaciones anidadas.

### 4. Listar, crear, ver uno, editar (PUT/PATCH) y borrar — las 5 operaciones CRUD completas con solo definir `queryset` y `serializer_class`.

### 5. Genera automáticamente todas las URLs de un ViewSet (GET, POST, PUT, PATCH, DELETE) sin tener que escribirlas manualmente una por una.

### 6. El bug: el permiso permitía **leer sin estar autenticado** (devolvía `True` para métodos seguros sin verificar login primero). Lo arreglamos agregando una verificación de `is_authenticated` **antes** de revisar si el método era de lectura o escritura.

### 7. El **access token** es de corta duración (60 min) y se usa en cada petición. El **refresh token** dura más (7 días) y sirve para pedir un access token nuevo sin volver a loguearse con usuario/contraseña.

### 8. Para evitar que un cliente malicioso mande un precio distinto al real (ej: comprar una hamburguesa de $15.000 diciendo que cuesta $100). El servidor SIEMPRE debe ser la fuente de verdad para el precio.

### 9. **403 Forbidden**. Porque el permiso `EsAdminOSoloLectura` exige `rol == 'admin'` para operaciones de escritura (POST/PUT/PATCH/DELETE), y el mesero no cumple esa condición.

### 10. `select_related` trae datos de una relación **uno-a-uno o muchos-a-uno** (ej: Producto→Categoria) en la MISMA consulta SQL. `prefetch_related` hace lo mismo para relaciones **uno-a-muchos** (ej: Venta→sus DetalleVenta). Ambos evitan el problema "N+1 queries" (una consulta extra por cada fila), haciendo la API más rápida.

---

## 🎯 Tu puntaje

- 🟢 **8-10**: Excelente, tienes una API REST funcional y segura
- 🟡 **5-7**: Bien, repasa lo fallado
- 🔴 **0-4**: Relee las 3 clases de esta fase

---

## 🏆 Habilidades de entrevista desbloqueadas

- ✅ "¿Cómo construiste tu API REST?"
- ✅ "¿Cómo manejas permisos por rol de usuario?"
- ✅ "¿Cómo evitas que el cliente manipule precios u otros datos sensibles?"
- ✅ "¿Cómo funciona la autenticación en tu proyecto?"
- ✅ "Cuéntame de un bug que encontraste y cómo lo depuraste" (¡tienes uno real para contar!)

---

## ➡️ Siguiente

**FASE 6 — Conectar el frontend (React) con esta API: login, dashboard y la UI del POS**
