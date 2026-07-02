# 🧠 Quiz FASE 4 — Modelos de base de datos

> 📚 **Clase que cubre**: [`04-modelos-django.md`](../clases/04-modelos-django.md)

---

## 📝 Preguntas

1. ¿Qué representa un Modelo de Django?
2. ¿Por qué usamos `DecimalField` y no `FloatField` para el precio?
3. ¿Qué hace un `ForeignKey`?
4. Si borro una Categoría y sus Productos usan `on_delete=PROTECT`, ¿qué pasa?
5. ¿Cuál es la diferencia entre `makemigrations` y `migrate`?
6. ¿Por qué separamos `Venta` de `DetalleVenta` en vez de un solo modelo?
7. ¿Para qué sirve `/admin` en Django?
8. ¿Por qué `Usuario` extiende `AbstractUser` en vez de crearse desde cero?
9. ¿Por qué `precio_unitario` se guarda en `DetalleVenta` en vez de solo consultar `producto.precio`?
10. ¿Qué tuvimos que hacer cuando agregamos `AUTH_USER_MODEL` después de la primera migración, y por qué?

---

---

---

## ✅ Respuestas

<br><br><br>

### 1. Una clase de Python que Django traduce automáticamente en una **tabla de base de datos**. Cada atributo de la clase es una columna.

### 2. Porque `FloatField` puede perder precisión en operaciones matemáticas (ej: `0.1 + 0.2` no da exactamente `0.3` en muchos lenguajes). En un sistema de ventas eso puede causar descuadres de dinero reales.

### 3. Crea una **relación entre tablas**: dice que un registro "pertenece a" un registro de otra tabla (ej: un Producto pertenece a una Categoría).

### 4. `PROTECT` **impide borrar** la Categoría mientras tenga Productos asociados — Django lanza un error para evitar perder la relación.

### 5. `makemigrations` **genera el plan de cambios** (un archivo Python describiendo qué cambió). `migrate` **ejecuta ese plan** contra la base de datos real.

### 6. Porque una Venta puede tener **múltiples productos**. `Venta` es la "factura completa" (quién, cuándo, total). `DetalleVenta` es **cada línea** de esa factura (qué producto, cuántas unidades).

### 7. Da un **panel de administración web automático** para crear, editar y borrar registros sin escribir HTML ni código adicional — solo hay que "registrar" el modelo.

### 8. Porque `AbstractUser` ya trae **gratis**: contraseñas encriptadas, sistema de permisos, compatibilidad con login/logout y con el Admin. Crear un sistema de autenticación desde cero sería reinventar la rueda (y probablemente menos seguro).

### 9. Porque es una **"fotografía" del precio al momento de la venta**. Si el producto sube de precio después, las ventas históricas NO deben cambiar — reflejan lo que realmente se cobró ese día.

### 10. Tuvimos que **borrar la base de datos SQLite y las migraciones existentes**, y regenerar todo desde cero. Esto es porque `AUTH_USER_MODEL` define la tabla de usuarios base del sistema, y Django no permite cambiarla después de que ya existen datos/migraciones con el modelo anterior — por eso se recomienda definirla **desde el inicio** del proyecto.

---

## 🎯 Tu puntaje

- 🟢 **8-10**: Perfecto, sigues a FASE 5
- 🟡 **5-7**: Bien, repasa lo fallado
- 🔴 **0-4**: Relee la clase 04

---

## 🏆 Habilidades de entrevista desbloqueadas

- ✅ "¿Cómo modelaste la base de datos de tu proyecto?"
- ✅ "¿Cómo manejas el dinero/precios en tu sistema?"
- ✅ "¿Cómo extendiste el sistema de usuarios de Django?"
- ✅ "¿Por qué separaste Venta y DetalleVenta?"

---

## ➡️ Siguiente

**FASE 5 — API REST con Serializers, ViewSets y autenticación JWT**
