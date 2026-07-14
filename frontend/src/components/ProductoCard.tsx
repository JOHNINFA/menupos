// Componente reutilizable: UNA tarjeta de producto.
// Ver mini-clase: docs/clases/08-componentes-props.md

import type { Producto } from '../types'

interface ProductoCardProps {
  producto: Producto
  onAgregar: (producto: Producto) => void
}

export function ProductoCard({ producto, onAgregar }: ProductoCardProps) {
  return (
    <button
      onClick={() => onAgregar(producto)}
      className="rounded-lg bg-white shadow hover:shadow-md text-left transition-shadow overflow-hidden flex flex-col"
    >
      {/* Imagen del producto (viene de Cloudinary). Si el producto no
          tiene imagen, mostramos un placeholder con un ícono. */}
      {producto.imagen ? (
        <div className="w-full h-40 bg-slate-50 flex items-center justify-center">
          <img
            src={producto.imagen}
            alt={producto.nombre}
            className="w-full h-full object-contain"
          />
        </div>
      ) : (
        <div className="w-full h-40 bg-slate-100 flex items-center justify-center text-4xl">
          🍽️
        </div>
      )}

      <div className="p-4">
        <h3 className="font-semibold text-slate-800">{producto.nombre}</h3>
        <p className="text-sm text-slate-500">{producto.categoria_nombre}</p>
        <p className="mt-2 font-bold text-orange-600">
          ${Number(producto.precio).toLocaleString('es-CO')}
        </p>
      </div>
    </button>
  )
}
