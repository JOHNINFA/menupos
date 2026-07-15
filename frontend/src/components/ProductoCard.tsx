// Componente reutilizable: UNA tarjeta de producto (estilo tienda/POS).
// Ver mini-clase: docs/clases/08-componentes-props.md

import type { Producto } from '../types'

interface ProductoCardProps {
  producto: Producto
  onAgregar: (producto: Producto) => void
}

export function ProductoCard({ producto, onAgregar }: ProductoCardProps) {
  return (
    <div className="rounded-2xl bg-white shadow-sm hover:shadow-md transition-shadow overflow-hidden flex flex-col">
      {/* Imagen del producto (Cloudinary) o placeholder si no tiene */}
      {producto.imagen ? (
        <img
          src={producto.imagen}
          alt={producto.nombre}
          className="w-full h-28 object-cover"
        />
      ) : (
        <div className="w-full h-28 bg-slate-100 flex items-center justify-center text-3xl">
          🍽️
        </div>
      )}

      <div className="p-3 flex flex-col">
        <p className="text-[10px] font-bold text-orange-500 uppercase tracking-wide">
          {producto.categoria_nombre}
        </p>
        <h3 className="font-semibold text-sm text-slate-800 leading-tight line-clamp-1">
          {producto.nombre}
        </h3>

        <div className="flex items-center justify-between mt-2">
          <p className="font-bold text-slate-800 text-sm">
            ${Number(producto.precio).toLocaleString('es-CO')}
          </p>
          {/* Botón "+" naranja para agregar al pedido */}
          <button
            onClick={() => onAgregar(producto)}
            className="w-8 h-8 rounded-full bg-orange-500 text-white text-lg leading-none flex items-center justify-center hover:bg-orange-600 shadow-sm transition-colors"
            aria-label={`Agregar ${producto.nombre}`}
          >
            +
          </button>
        </div>
      </div>
    </div>
  )
}
