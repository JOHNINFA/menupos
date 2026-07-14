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
      className="rounded-2xl bg-white shadow-sm hover:shadow-md text-left transition-shadow overflow-hidden flex flex-col"
    >
      {/* Imagen del producto (viene de Cloudinary). Si no tiene, placeholder. */}
      {producto.imagen ? (
        <div className="w-full aspect-square bg-slate-50 flex items-center justify-center">
          <img
            src={producto.imagen}
            alt={producto.nombre}
            className="w-full h-full object-cover"
          />
        </div>
      ) : (
        <div className="w-full aspect-square bg-slate-100 flex items-center justify-center text-3xl">
          🍽️
        </div>
      )}

      <div className="p-2.5">
        <h3 className="font-semibold text-sm text-slate-800 leading-tight line-clamp-1">
          {producto.nombre}
        </h3>
        <p className="text-xs text-slate-400">{producto.categoria_nombre}</p>
        <p className="mt-1 font-bold text-orange-600 text-sm">
          ${Number(producto.precio).toLocaleString('es-CO')}
        </p>
      </div>
    </button>
  )
}
