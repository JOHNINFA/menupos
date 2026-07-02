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
      className="p-4 rounded-lg bg-white shadow hover:shadow-md text-left transition-shadow"
    >
      <h3 className="font-semibold text-slate-800">{producto.nombre}</h3>
      <p className="text-sm text-slate-500">{producto.categoria_nombre}</p>
      <p className="mt-2 font-bold text-orange-600">
        ${Number(producto.precio).toLocaleString('es-CO')}
      </p>
    </button>
  )
}
