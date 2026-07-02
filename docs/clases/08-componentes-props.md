# 📖 Clase 08 — Componentes y Props en React

> 🎯 **Objetivo**: Entender cómo se pasan datos entre componentes.
> ⏱️ **Tiempo**: 6 minutos
> 📚 **Pre-requisitos**: Clase [`03-react-vite-tailwind.md`](03-react-vite-tailwind.md)

---

## 🧩 Recordatorio

Un componente es un **molde de galleta** (Clase 03). Las **props** son el "sabor" que le das a cada galleta cuando la usas.

## 💻 Ejemplo: `ProductoCard`

```tsx
// El componente RECIBE props como parámetros (aquí desestructurados)
interface ProductoCardProps {
  nombre: string
  precio: number
  onAgregar: () => void   // una función que el padre le pasa al hijo
}

function ProductoCard({ nombre, precio, onAgregar }: ProductoCardProps) {
  return (
    <div className="p-4 rounded-lg bg-white shadow">
      <h3>{nombre}</h3>
      <p>${precio}</p>
      <button onClick={onAgregar}>Agregar</button>
    </div>
  )
}
```

Y se usa así, "estampando el molde" con datos distintos cada vez:

```tsx
<ProductoCard nombre="Hamburguesa" precio={15000} onAgregar={() => agregarAlCarrito(1)} />
<ProductoCard nombre="Jugo de Mora" precio={6000} onAgregar={() => agregarAlCarrito(2)} />
```

## 🔑 Regla de oro

**Las props fluyen en UNA sola dirección: de padre a hijo.** Un componente hijo NUNCA modifica directamente las props que recibió — si necesita "avisar" algo al padre, le pasan una **función** (como `onAgregar` arriba) y el hijo la llama.

### Analogía
Las props son como el **pedido que el mesero (padre) le entrega a la cocina (hijo)**: la cocina no decide el pedido, solo lo recibe y actúa según lo que le llegó.

---

## 🧠 Quiz rápido
1. ¿En qué dirección fluyen las props?
2. ¿Cómo le avisa un componente hijo algo a su padre?

> 📝 Respuestas en el quiz de FASE 6.
