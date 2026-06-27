# 🧠 Quiz FASE 1 — Conceptos básicos

> 📚 **Clases que cubre**: [`00-bienvenida.md`](../clases/00-bienvenida.md), [`01-arquitectura.md`](../clases/01-arquitectura.md)
> 📊 **Diagrama relacionado**: [`01-vision-general.md`](../diagramas/01-vision-general.md)
> 🎯 **Objetivo**: Verificar que entendiste qué es MenuPOS, cómo está organizado y cómo funciona la comunicación frontend/backend.

---

## ⚠️ Instrucciones

1. **Intenta responder TODAS las preguntas** antes de mirar las respuestas
2. Escribe tu respuesta mental o en una hoja aparte
3. Después de las 10 preguntas, abre las respuestas
4. Si fallaste 3 o más, **relee las clases** antes de continuar a FASE 2

---

## 📝 Preguntas

### 1. ¿Qué significan las siglas **POS**?
> _Pista_: aparece en la primera frase de la bienvenida.

### 2. ¿Qué dos tipos de usuarios va a tener MenuPOS?

### 3. En la metáfora del restaurante, ¿qué representa el **backend**?

### 4. ¿Y qué representa el **serializer**?

### 5. ¿Por qué decidimos usar analogías del restaurante para aprender?

### 6. ¿Dónde "vive" el frontend: en el servidor o en el navegador?

### 7. ¿En qué se diferencian los verbos HTTP `GET` y `POST`?

### 8. ¿En qué "idioma" se comunican el frontend y el backend?

### 9. Si quiero **eliminar** un producto, ¿qué verbo HTTP debería usar?

### 10. Si quiero pedir **la lista de productos** a la API, ¿cómo se vería la URL y el verbo?

---

---

---

## ✅ Respuestas

> ⚠️ **¡No mires aún si no respondiste arriba!**

<br><br><br>

### 1. **POS** = Point Of Sale (Punto de Venta).
Es el sistema que usan los restaurantes/tiendas para registrar cada venta.

### 2. **Administrador** (gestiona el menú, ve métricas) y **Mesero** (toma pedidos y cobra).

### 3. El backend representa la **cocina + administración** del restaurante: todo lo que el cliente NO ve directamente. Procesa pedidos, guarda la información, calcula totales, genera reportes.

### 4. El serializer es el **mesero traductor**. Traduce entre el "idioma" de la cocina (objetos Python) y el "idioma" del cliente (JSON). Sin él, el cliente y la cocina no podrían entenderse.

### 5. Porque los conceptos técnicos (Modelos, Serializers, ViewSets) son **abstractos y confusos** si los aprendes en abstracto, pero **clarísimos** si los piensas como partes de un restaurante. Como MenuPOS ES un restaurante virtual, la metáfora calza perfectamente y te ayuda a recordar.

### 6. El frontend vive en el **navegador del cliente** (Chrome, Firefox, etc.). Cuando un usuario abre tu página, su navegador descarga el código JavaScript y lo ejecuta localmente.

### 7. - **`GET`** = "Dame algo" (consultar/leer). No modifica nada.
   - **`POST`** = "Crea algo nuevo". Cambia el estado del servidor.

   Ejemplo: `GET /api/productos/` lee la lista. `POST /api/productos/` crea uno nuevo.

### 8. En **JSON** (JavaScript Object Notation). Es un formato de texto con claves y valores, parecido a un diccionario en Python.

### 9. Verbo **`DELETE`**.
   Ejemplo: `DELETE /api/productos/5/` elimina el producto con ID 5.

### 10. Verbo **`GET`**, URL **`/api/productos/`**.
   Forma completa: `GET /api/productos/` → devuelve un array JSON con todos los productos.

---

## 🎯 Tu puntaje

- 🟢 **8-10 correctas**: ¡Excelente! Estás listo para FASE 2.
- 🟡 **5-7 correctas**: Bien, pero relee las partes que fallaste antes de continuar.
- 🔴 **0-4 correctas**: Vuelve a leer ambas clases con calma. No hay prisa.

---

## 🏆 Habilidades de entrevista desbloqueadas

Con FASE 1 superada, puedes responder con confianza:

- ✅ "¿De qué trata tu proyecto?"
- ✅ "¿Qué es una API REST?"
- ✅ "¿Cuál es la diferencia entre frontend y backend?"
- ✅ "¿Qué verbos HTTP conoces?"
- ✅ "¿Qué formato usan tus APIs para comunicarse?"

---

## ➡️ Siguiente

Cuando estés listo: **FASE 2 — Setup Django + DRF backend**.
