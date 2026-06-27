# 📖 Clase 01 — Arquitectura: Frontend, Backend y API

> 🎯 **Objetivo**: Entender cómo se comunican el "salón" y la "cocina" del restaurante.
> ⏱️ **Tiempo**: 8 minutos
> 📚 **Pre-requisitos**: Haber leído [`00-bienvenida.md`](00-bienvenida.md)

---

## 🤔 El problema

Imagina que tienes que construir MenuPOS **TODO EN UN SOLO PROGRAMA**:

- La pantalla bonita que ve el mesero
- La lógica para guardar ventas
- Las consultas a la base de datos
- La generación de tickets

❌ **Problema**: Todo mezclado = un caos imposible de mantener.

✅ **Solución**: Separamos en **2 partes** que se comunican entre sí.

---

## 🏗️ La separación clave: Frontend vs Backend

### 🎨 Frontend = "Lo que el usuario VE"

Todo lo visual:
- La página de login
- El menú con los productos
- Los botones
- Los formularios
- Los colores

> 📍 **Vive en**: el navegador del cliente (Chrome, Firefox, etc.)
> 🛠️ **Lo construimos con**: React + Vite + Tailwind

### ⚙️ Backend = "Lo que el usuario NO VE"

Toda la lógica oculta:
- Verificar usuario y contraseña
- Guardar las ventas en la base de datos
- Calcular el total con impuestos
- Generar reportes
- Servir las imágenes

> 📍 **Vive en**: un servidor en internet (en nuestro caso, Railway)
> 🛠️ **Lo construimos con**: Django + DRF + PostgreSQL

---

## 🍽️ La analogía del restaurante (otra vez, con detalle)

### 🎨 Frontend = Salón / Comedor del restaurante
Lo que ve el cliente cuando entra:
- 🪑 Las mesas (formularios)
- 📋 La carta del menú (lista de productos)
- 🛎️ La campanita para llamar al mesero (botones)
- 🎵 La música ambiente (estilos / Tailwind)

### ⚙️ Backend = Cocina + Bodega + Administración
Lo que el cliente NO ve:
- 🍳 La cocina (lógica del negocio)
- ❄️ El refrigerador (base de datos)
- 📒 El libro contable (ventas registradas)
- 🔐 La caja fuerte con contratos (datos privados)

### 🧑‍💼 El mesero conecta los dos
El mesero (que llamamos **API** en el código):
- Recibe el pedido del cliente
- Lo lleva a la cocina
- Trae lo que la cocina prepara
- Lo entrega al cliente

**Sin el mesero**, el cliente nunca podría comunicarse con la cocina. Sin la **API**, el frontend nunca podría comunicarse con el backend.

---

## 🌐 ¿Qué es una API REST?

**API** = Application Programming Interface = "Interfaz para que dos programas hablen entre sí".

**REST** = un conjunto de **reglas** sobre cómo deben hablar.

### Las 4 acciones básicas de una API REST

Igual que un mesero solo hace 4 cosas básicas:

| Acción del mesero | Verbo HTTP | Ejemplo en MenuPOS |
|---|---|---|
| 🔍 **Mostrarte el menú** | `GET` | "Dame la lista de productos" |
| ➕ **Tomar tu pedido nuevo** | `POST` | "Crea una venta nueva" |
| ✏️ **Cambiar tu pedido** | `PUT` o `PATCH` | "Cambia el precio del producto X" |
| ❌ **Cancelar tu pedido** | `DELETE` | "Borra el producto X del menú" |

### Las URLs son las "direcciones" para pedir cosas

Cada acción tiene su dirección. En MenuPOS van a ser así:

```
GET    /api/productos/       → Lista todos los productos
POST   /api/productos/       → Crea un producto nuevo
GET    /api/productos/5/     → Trae el producto con ID 5
PUT    /api/productos/5/     → Modifica el producto con ID 5
DELETE /api/productos/5/     → Elimina el producto con ID 5
```

> 💡 Fíjate el patrón: la **URL** es siempre la misma; el **verbo** cambia según lo que quieras hacer.

---

## 💬 Cómo se "hablan" frontend y backend (en JSON)

El mesero no habla "comida". Habla en español (o el idioma del cliente).

Frontend y backend se hablan en un idioma común: **JSON**.

### Ejemplo de un producto en JSON

```json
{
  "id": 7,
  "nombre": "Hamburguesa Clásica",
  "precio": 15000,
  "descripcion": "Carne 150g, queso, lechuga, tomate",
  "categoria": "Hamburguesas",
  "imagen_url": "https://s3.../hamburguesa.jpg"
}
```

JSON es como un diccionario:
- 🔑 **Claves** a la izquierda (`"nombre"`)
- 📦 **Valores** a la derecha (`"Hamburguesa Clásica"`)
- ✂️ Separados con `:`

---

## 🎬 Cómo es UNA petición completa (paso a paso)

Imaginemos que el mesero (frontend) le pide la lista de productos a la cocina (backend):

```
1. 🧑‍💼 Mesero: "Necesito la lista de productos"
2. 🚪 Pasa por la puerta (URL): /api/productos/
3. 👀 Usa el verbo correcto: GET
4. ⏳ La petición VIAJA por internet
5. 🍳 La cocina (Django) recibe
6. 📋 La cocina consulta la base de datos (PostgreSQL)
7. 📦 Empaqueta la respuesta en JSON
8. ⏳ La respuesta VIAJA de vuelta
9. ✅ El mesero recibe la lista
10. 🎨 El frontend pinta los productos en pantalla
```

Todo eso pasa en **menos de 1 segundo**. ¡Esa es la magia!

---

## 🧠 Quiz rápido de la Clase 01

1. ¿En qué parte vive el frontend, en el servidor o en el navegador?
2. ¿En qué se diferencian `GET` y `POST`?
3. ¿En qué "idioma" se hablan frontend y backend?
4. ¿Qué hace el "mesero" (API) en la analogía?
5. Si quiero borrar un producto, ¿qué verbo HTTP uso?

> 📝 Respuestas al final del quiz de la FASE 1.

---

## 🎯 Lo que aprendiste hasta aquí

Después de las 2 primeras clases puedes responder estas preguntas de entrevista:

- ✅ "¿Qué hace tu proyecto MenuPOS?"
- ✅ "¿Cuál es la diferencia entre frontend y backend?"
- ✅ "¿Qué es una API REST?"
- ✅ "¿Para qué sirve JSON?"

---

## ➡️ Siguiente clase

📖 (Próximamente) `02-que-es-un-modelo.md` — Cuando creemos el primer modelo en Django.

📊 Antes de seguir, mira el diagrama: [`../diagramas/01-vision-general.md`](../diagramas/01-vision-general.md)

---

## 🔗 Referencias

- [REST API explicada (MDN)](https://developer.mozilla.org/es/docs/Glossary/REST) (Mozilla, en español)
- [Verbos HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Methods) (Mozilla, en español)
- [JSON explicado](https://www.w3schools.com/whatis/whatis_json.asp) (W3Schools, en inglés)
