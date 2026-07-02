# 📖 Clase 00 — Bienvenido a MenuPOS

> 🎯 **Objetivo de esta clase**: Entender qué vas a construir, para quién y por qué.
> ⏱️ **Tiempo de lectura**: 7 minutos
> 📚 **Pre-requisitos**: Ninguno

---

## 🍔 ¿Qué es MenuPOS?

MenuPOS es un **sistema de punto de venta (POS)** para restaurantes pequeños.

> **POS** = "Point Of Sale" en inglés = "Punto de Venta" en español.
> Es el computador/tablet donde el restaurante registra cada venta.

### Imagínate esto

Vas a un restaurante. Pides una hamburguesa y una Coca-Cola. El mesero saca su tablet, toca **🍔 Hamburguesa**, toca **🥤 Coca-Cola**, ve el total `$25.000`, te cobra, e imprime un ticket.

**ESO** es lo que hace un POS. **ESO** es lo que vas a construir.

---

## 👥 ¿Para quién es?

Para 2 tipos de usuarios:

### 1. El **administrador del restaurante** 👔
- Crea los productos del menú
- Sube las fotos
- Define los precios
- Ve las ventas del día/mes
- Sabe qué productos se venden más

### 2. El **mesero** 🧑‍💼
- Hace login al iniciar su turno
- Toma pedidos en la pantalla
- Cobra y cierra cada venta
- Ve su historial de ventas del día

---

## 🤔 ¿Qué problemas resuelve?

Antes (sin sistema POS):
- 📝 Apuntar pedidos en papel → se pierden, se olvidan
- 🧮 Sumar precios con calculadora → errores
- 📊 Saber qué se vendió hoy → imposible sin contar manualmente
- 💰 Saber cuánto facturó el mes → adivinanza

Con MenuPOS:
- ✅ Cada venta queda registrada automáticamente
- ✅ El total se calcula solo
- ✅ Hay un dashboard con métricas en tiempo real
- ✅ Las ventas se guardan en una base de datos para siempre

---

## 🎬 La metáfora del restaurante (¡IMPORTANTE!)

A lo largo de TODAS las clases vamos a usar **analogías con un restaurante real**.

¿Por qué? Porque MenuPOS **es** un restaurante (virtual). Y los conceptos técnicos de Django y React son confusos si los aprendes en abstracto, pero **clarísimos** si los piensas como partes de un restaurante.

### Mapa de equivalencias

| 🧑‍💻 Concepto técnico | 🍽️ Equivalente en el restaurante |
|---|---|
| **Modelo** (en Django) | La **receta** guardada en la cocina (estructura de un producto) |
| **Base de datos** | La **despensa/refrigerador** (donde se guarda todo) |
| **Migración** | **Remodelación** del local (cambio en la estructura) |
| **Serializer** | El **mesero traductor** (traduce entre cocina y cliente) |
| **ViewSet** | El **comedor** (donde llegan los pedidos del cliente) |
| **URL** | La **puerta** del restaurante (la dirección por donde se entra) |
| **API REST** | El **sistema de comandas** (cómo se piden las cosas) |
| **JWT (token)** | La **pulsera VIP** que te dan al entrar (prueba que pagaste cover) |
| **Frontend** | El **restaurante físico** (lo que ve el cliente) |
| **Backend** | La **cocina + administración** (lo que NO ve el cliente) |
| **PostgreSQL** | El **inventario** organizado en estantes |
| **AWS S3** | La **galería de fotos** colgada en la pared |

> 💡 **Tip**: Cuando algo te parezca confuso, vuelve a esta tabla y piensa en la analogía. Casi siempre se aclara.

---

## 🗺️ ¿Cómo está organizado el proyecto?

```
menupos/                    ← La carpeta principal
│
├── 📁 backend/             ← La COCINA del restaurante
│   │                         (donde se procesan los pedidos,
│   │                          se guardan los datos, etc.)
│   └── (Django + Python)
│
├── 📁 frontend/            ← El SALÓN del restaurante
│   │                         (lo que ve y usa el cliente)
│   └── (React + TypeScript)
│
├── 📁 docs/                ← Tu CURSO PERSONAL
│   ├── clases/             ← Mini-clases como esta
│   ├── diagramas/          ← Visualizaciones
│   └── quizzes/            ← Preguntas para repasar
│
├── 📄 README.md            ← Carta de presentación del proyecto
├── 📄 CLAUDE.md            ← Instrucciones para Claude AI
├── 📄 .gitignore           ← Lista de cosas a ignorar en Git
└── 📄 .env.example         ← Plantilla de variables secretas
```

---

## 🛠️ Las herramientas que vamos a usar

### Backend (la cocina)
- **Python 3.10+** → El lenguaje
- **Django 5** → El framework (= "kit de herramientas") principal
- **Django REST Framework (DRF)** → Para crear APIs fácilmente
- **PostgreSQL** → La base de datos profesional

### Frontend (el salón)
- **React** → Para construir interfaces interactivas
- **Vite** → Para que React arranque rápido en desarrollo
- **TypeScript** → JavaScript pero con "tipos" (más seguro)
- **Tailwind CSS** → Estilos rápidos sin escribir CSS tradicional
- **shadcn/ui** → Componentes bonitos listos (botones, modales, etc.)

### Servicios externos
- **AWS S3** → Donde guardamos las imágenes
- **Railway** → Donde "publicaremos" el backend al final
- **Vercel** → Donde "publicaremos" el frontend al final

> ⚠️ **No te preocupes por todos estos nombres ahora**. Los vamos a usar uno por uno cuando llegue su momento. Cada uno tendrá su propia mini-clase.

---

## 🚦 ¿Cuáles son los pasos a seguir?

Vamos por **fases pequeñas** para no abrumarte:

```
✅ FASE 1: Estructura + esta clase y otras iniciales       ← AQUÍ ESTAMOS
⏳ FASE 2: Instalar Django y arrancar el backend
⏳ FASE 3: Instalar React y arrancar el frontend
⏳ FASE 4: Crear los modelos (estructuras de datos)
⏳ FASE 5: Crear los serializers y la API REST
⏳ FASE 6: Autenticación con JWT
⏳ FASE 7: Construir la UI del POS
⏳ FASE 8: Subir imágenes a AWS S3
⏳ FASE 9: Deploy (publicar en internet)
⏳ FASE 10: README final con screenshots y GIF demo
```

---

## 🧠 Quiz de la Clase 00

Responde mentalmente (o escríbelas en `docs/quizzes/fase-01.md` cuando llegue el momento):

1. ¿Qué significan las siglas **POS**? respuesta : sistema de punto de venta
2. ¿Qué dos tipos de usuarios va a tener MenuPOS? respuestas: administrador y meseroa
3. En la metáfora del restaurante, ¿qué representa el **backend**? es la cocina y administracion lo quen no se ve
4. ¿Qué representa el **serializer**? es el traductor
5. ¿Por qué usamos analogías del restaurante para aprender? es mas facil de entender sobre la practica

> 📝 Las respuestas las verás resueltas en `docs/quizzes/fase-01.md` al final de la FASE 1.

---

## ➡️ Siguiente clase

📖 [`01-arquitectura.md`](01-arquitectura.md) — Cómo se conectan el frontend y el backend (con diagrama).

---

## 🔗 Referencias para profundizar (opcional)

- [¿Qué es Django?](https://www.djangoproject.com/) (sitio oficial, en inglés)
- [¿Qué es React?](https://es.react.dev/) (sitio oficial, en español)
- [¿Qué es una API REST?](https://aws.amazon.com/es/what-is/restful-api/) (explicación de AWS, en español)

---

> 💬 **¿Te quedó alguna duda?** Pregúntale a Claude antes de continuar.
> No avances si algo no está claro — las próximas clases asumen que entendiste esta.
