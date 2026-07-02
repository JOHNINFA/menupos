# 📖 Clase 03 — React, Vite y Tailwind (el "salón" del restaurante)

> 🎯 **Objetivo**: Entender qué es React, para qué sirve Vite, y cómo Tailwind nos ahorra escribir CSS.
> ⏱️ **Tiempo**: 10 minutos
> 📚 **Pre-requisitos**: Clase [`01-arquitectura.md`](01-arquitectura.md)

---

## 🎨 Recordatorio rápido

El **frontend es el salón** del restaurante: todo lo que el cliente (mesero) ve y toca. Lo construimos con **React**.

---

## ⚛️ Parte 1: ¿Qué es React?

React es una librería de JavaScript para construir **interfaces hechas de piezas reutilizables** llamadas **componentes**.

### El problema sin React
Si construyes una web con HTML/JS "a mano":
- Cada vez que cambia un dato, tienes que **buscar manualmente** el elemento en la página y actualizarlo
- El código se vuelve espagueti rápido
- Reutilizar una pieza visual en 5 lugares distintos = copiar y pegar 5 veces

### La solución de React
Divides la interfaz en **piezas (componentes)**:

```
🍽️ Pantalla del POS
├── 🧩 <Header />           → la barra superior
├── 🧩 <ListaProductos />   → la lista de productos del menú
│    └── 🧩 <ProductoCard />  → UNA tarjeta de producto (se repite N veces)
├── 🧩 <Carrito />          → el carrito de compra actual
└── 🧩 <BotonCobrar />      → el botón para cerrar la venta
```

Cada componente:
- Se programa **UNA vez**
- Se puede **reutilizar** cuantas veces quieras
- React se encarga de **actualizar solo lo que cambió** en pantalla (eficiente)

### Analogía
Un componente de React es como un **molde de galleta** 🍪:
- Programas el molde una vez (ej: `<ProductoCard />`)
- Lo "estampas" tantas veces como productos tengas
- Cada galleta (instancia) puede tener su propio "sabor" (datos: nombre, precio, imagen)

---

## ⚡ Parte 2: ¿Qué es Vite?

**Vite** (se pronuncia "vit", del francés "rápido") es la **herramienta que arma y sirve** tu proyecto de React mientras programas.

### El problema sin Vite
Antes, herramientas como Webpack tardaban **segundos o minutos** en recompilar cada vez que guardabas un archivo. Muy lento para programar.

### La solución de Vite
- Arranca el servidor de desarrollo en **milisegundos**
- Cuando guardas un archivo, actualiza SOLO esa parte en el navegador (sin recargar toda la página) — esto se llama **HMR** (Hot Module Replacement)
- Cuando terminas, empaqueta todo para producción de forma optimizada (`npm run build`)

### Analogía
Si React son los **ingredientes y la receta**, Vite es la **cocina exprés** que te permite probar el plato al instante sin esperar que el horno caliente cada vez.

---

## 🎨 Parte 3: ¿Qué es Tailwind CSS?

### El problema sin Tailwind
CSS tradicional requiere:
1. Escribir una clase en el HTML: `<div class="tarjeta-producto">`
2. Ir a un archivo `.css` aparte
3. Definir: `.tarjeta-producto { padding: 16px; border-radius: 8px; ... }`
4. Repetir esto para CADA estilo nuevo

Con proyectos grandes, terminas con miles de líneas de CSS difíciles de rastrear.

### La solución de Tailwind
Tailwind te da **clases utilitarias ya hechas** que aplicas directo en el HTML/JSX:

```jsx
<div className="p-4 rounded-lg bg-white shadow-md">
  Tarjeta de producto
</div>
```

Donde:
- `p-4` = padding de 1rem (16px)
- `rounded-lg` = bordes redondeados grandes
- `bg-white` = fondo blanco
- `shadow-md` = sombra media

**No escribes CSS nuevo.** Combinas piezas ya armadas, como piezas de LEGO.

### Analogía
- CSS tradicional = **coser tu propia ropa** desde cero cada vez
- Tailwind = **combinar piezas de un guardarropa ya armado** (esta camisa + este pantalón)

---

## 🛠️ Lo que instalamos en FASE 3

```bash
npm create vite@latest frontend -- --template react-ts   # Arma el esqueleto
npm install                                                # Instala dependencias base
npm install tailwindcss @tailwindcss/vite                  # Tailwind CSS v4
npm install react-router-dom axios                          # Rutas + peticiones HTTP
```

| Paquete | Para qué sirve |
|---|---|
| `react` + `react-dom` | El núcleo de React |
| `vite` + `@vitejs/plugin-react` | El motor de desarrollo |
| `typescript` | JavaScript con "tipos" (detecta errores antes de ejecutar) |
| `tailwindcss` + `@tailwindcss/vite` | Estilos utilitarios |
| `react-router-dom` | Manejar rutas (ej: `/login`, `/pos`, `/dashboard`) — lo usaremos en FASE 6 |
| `axios` | Hacer peticiones HTTP a nuestra API de Django — lo usaremos en FASE 5-6 |

---

## 📂 Estructura del frontend

```
frontend/
├── 📁 src/
│   ├── App.tsx          ← Componente raíz (por ahora, pantalla de bienvenida)
│   ├── main.tsx          ← Punto de entrada: monta <App /> en el HTML
│   ├── index.css          ← Solo tiene: @import "tailwindcss";
│   └── assets/            ← Imágenes, iconos, etc.
├── 📄 index.html          ← El único archivo HTML real (React pinta todo dentro)
├── 📄 vite.config.ts       ← Configuración de Vite (plugins de React y Tailwind)
├── 📄 package.json         ← Lista de dependencias (el "requirements.txt" de Node)
└── 📄 tsconfig.json        ← Configuración de TypeScript
```

> 💡 Fíjate: **no hay** `tailwind.config.js`. En Tailwind v4, la configuración vive directamente en el CSS con `@import "tailwindcss"` — mucho más simple que versiones anteriores.

---

## 🧠 Quiz rápido

1. ¿Qué es un componente en React? Da un ejemplo de MenuPOS.
2. ¿Cuál es la ventaja principal de Vite frente a herramientas más viejas?
3. ¿Qué significa HMR?
4. ¿Cómo se aplican estilos con Tailwind, en una frase?
5. ¿Qué hace `npm run build` a diferencia de `npm run dev`?

> 📝 Respuestas en el quiz de FASE 3.

---

## ➡️ Qué sigue

Con el frontend funcionando (FASE 3 lista), en **FASE 4** vamos a crear los **Modelos** en Django: la estructura de datos de usuarios, productos y ventas.

---

## 🔗 Referencias

- [React (documentación oficial, español)](https://es.react.dev/)
- [Vite (documentación oficial)](https://vite.dev/guide/)
- [Tailwind CSS v4 (documentación oficial)](https://tailwindcss.com/docs)
