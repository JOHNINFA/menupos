# 📖 Clase 09 — Estado (useState) y Efectos (useEffect)

> 🎯 **Objetivo**: Entender cómo React recuerda datos que cambian y cómo reacciona a eventos como "cargar la página".
> ⏱️ **Tiempo**: 8 minutos
> 📚 **Pre-requisitos**: Clase [`08-componentes-props.md`](08-componentes-props.md)

---

## 🧠 `useState` — la memoria de un componente

Un componente necesita "recordar" cosas que cambian (ej: qué hay en el carrito). Para eso usamos `useState`:

```tsx
import { useState } from 'react'

function Pos() {
  // carrito = el valor actual. setCarrito = la función para CAMBIARLO.
  const [carrito, setCarrito] = useState<Item[]>([])

  function agregarProducto(producto: Producto) {
    setCarrito([...carrito, producto])  // nunca modifiques el array directo
  }

  return <div>Productos en el carrito: {carrito.length}</div>
}
```

### Regla de oro
**Nunca modifiques el estado directamente** (`carrito.push(x)` ❌). Siempre usa la función `set...` con un valor NUEVO (`setCarrito([...carrito, x])` ✅). Así React sabe que algo cambió y vuelve a pintar la pantalla.

### Analogía
`useState` es como una **pizarra en la cocina** donde anotas el pedido actual. Si borras y reescribes directamente sin avisar al mesero (React), el mesero no se entera del cambio. `setCarrito(...)` es "avisarle oficialmente" al mesero que la pizarra cambió.

---

## ⏱️ `useEffect` — reaccionar a eventos

Necesitamos **pedir los productos a la API** apenas se abre la pantalla del POS. Eso es un "efecto secundario" (algo que pasa FUERA del flujo normal de pintar la pantalla).

```tsx
import { useState, useEffect } from 'react'

function Pos() {
  const [productos, setProductos] = useState<Producto[]>([])

  useEffect(() => {
    // Esta función se ejecuta cuando el componente aparece en pantalla
    api.get('/productos/').then((res) => setProductos(res.data))
  }, []) // ← el array vacío significa: "ejecuta esto SOLO una vez"

  return <div>{productos.length} productos cargados</div>
}
```

### El array de dependencias `[]`

| Array | Cuándo se ejecuta |
|---|---|
| `useEffect(fn, [])` | Solo UNA vez, cuando el componente aparece |
| `useEffect(fn, [carrito])` | Cada vez que `carrito` cambie |
| `useEffect(fn)` (sin array) | Después de CADA render (rara vez se usa así) |

### Analogía
`useEffect` es la **campanita que suena cuando el mesero entra al salón** ("ve y pregunta en cocina qué hay disponible hoy"). El array de dependencias decide CUÁNDO vuelve a sonar esa campanita.

---

## 🧠 Quiz rápido
1. ¿Por qué no se debe modificar el estado directamente?
2. ¿Qué hace el array vacío `[]` en `useEffect`?
3. ¿Cuándo usarías `useEffect` en MenuPOS?

> 📝 Respuestas en el quiz de FASE 6.

## 🔗 Referencias
- [useState (React docs, español)](https://es.react.dev/reference/react/useState)
- [useEffect (React docs, español)](https://es.react.dev/reference/react/useEffect)
