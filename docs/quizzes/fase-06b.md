# 🧠 Quiz FASE 6b — Flujo de negocio (estados, roles, cuenta abierta)

> 📚 **Clase que cubre**: [`11-estados-y-reglas-negocio.md`](../clases/11-estados-y-reglas-negocio.md)
> 🎯 Refinamientos que surgieron de probar la app como un restaurante real.

---

## 📝 Preguntas

1. ¿Qué es una máquina de estados, en una frase?
2. ¿Cuáles son los 4 estados de un pedido en MenuPOS y en qué orden van?
3. ¿Por qué el mesero puede marcar "entregado" pero NO "pagado"?
4. ¿Por qué el estado se cambia con un endpoint dedicado (`/marcar_estado/`) y no con un PATCH genérico?
5. ¿Por qué NO se debe confiar en el frontend para calcular el precio o el total?
6. ¿Qué pasa cuando una mesa con cuenta abierta pide otra bebida?
7. ¿Por qué `mesa` es un campo que puede ser nulo (null)?
8. Cuando el admin crea un mesero, ¿cómo se guarda la contraseña de forma segura?
9. ¿Qué bug apareció al crear un producto vía formulario (multipart) sin marcar "disponible", y cómo se arregló?
10. ¿Por qué reforzamos el permiso de ventas para mirar `view.action` en vez de solo `request.method`?

---

---

---

## ✅ Respuestas

<br><br><br>

### 1. Un modelo donde algo solo puede estar en uno de varios estados definidos y solo puede moverse entre ellos siguiendo reglas.

### 2. **Pedido → Entregado → Pagado**, más **Cancelado** (que puede ocurrir desde pedido o entregado). El pedido nace en "pedido" y termina en "pagado" o "cancelado".

### 3. Porque marcar "entregado" es parte del trabajo del mesero (él lleva los platos), pero "pagado" es una **decisión de caja** que afecta el dinero — solo el cajero/admin debe poder cerrarla.

### 4. Porque así el campo `estado` es de **solo lectura** en el serializer, y la única forma de cambiarlo pasa por las reglas de `marcar_estado` (validación de estado + permiso por rol). Un PATCH genérico permitiría intentar colar cambios de mesero/total/detalles junto con el estado.

### 5. Porque el frontend **se puede manipular** (cualquiera edita el JavaScript en su navegador). Si confiáramos en él, alguien podría pagar $1 por una comida de $50.000. El backend es la única fuente de verdad para el dinero.

### 6. Como la mesa tiene una cuenta **abierta** (estado pedido o entregado), el backend **suma** los nuevos productos a esa misma venta (no crea otra) y el total crece. Además la cuenta vuelve a estado "pedido" porque hay algo nuevo que preparar/entregar.

### 7. Porque un pedido **"Para llevar"** no tiene mesa. `mesa` solo se exige (y se valida) cuando el `tipo` es "mesa".

### 8. Con `Usuario.objects.create_user(...)`, que **encripta (hashea)** la contraseña antes de guardarla. Además el campo `password` es `write_only` en el serializer: se puede enviar al crear, pero la API nunca lo devuelve.

### 9. Al no enviar "disponible" en un formulario multipart, DRF lo tomaba como **False** (como un checkbox HTML sin marcar) en vez de usar el `default=True` del modelo — el producto quedaba oculto. Se arregló declarando `disponible = serializers.BooleanField(default=True)` explícitamente en el serializer.

### 10. Porque el ViewSet de ventas tiene una acción personalizada (`marcar_estado`) que viaja por **POST**, igual que `create`. Si el permiso mirara solo `request.method == 'POST'`, un mesero podría colarse a cambiar estados. Mirando `view.action` distinguimos "crear una venta" (permitido) de "marcar_estado" (con reglas propias).

---

## 🎯 Tu puntaje
- 🟢 **8-10**: Dominas la lógica de negocio de tu app
- 🟡 **5-7**: Repasa lo fallado
- 🔴 **0-4**: Relee la clase 11

## 🏆 Habilidades de entrevista desbloqueadas
- ✅ "¿Cómo modelaste el ciclo de vida de un pedido?"
- ✅ "¿Cómo garantizas que un usuario no manipule precios o estados?"
- ✅ "Cuéntame de un bug que encontraste al probar tu app" (¡tienes 3 reales!)
- ✅ "¿Cómo manejas permisos por rol a nivel de acción, no solo de endpoint?"

---

## ➡️ Siguiente
**FASE 7 — Imágenes de productos en AWS S3**
