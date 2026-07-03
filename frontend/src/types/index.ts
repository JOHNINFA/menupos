// Tipos TypeScript que reflejan lo que devuelve la API de Django.
// Tenerlos centralizados evita repetir estas formas en cada componente
// y hace que el editor te avise si usas un campo que no existe.

export interface Usuario {
  id: number
  username: string
  first_name: string
  last_name: string
  rol: 'admin' | 'mesero'
}

export interface Categoria {
  id: number
  nombre: string
}

export interface Producto {
  id: number
  nombre: string
  descripcion: string
  precio: string // DRF serializa DecimalField como string, no number
  categoria: number
  categoria_nombre: string
  imagen: string | null
  disponible: boolean
}

export interface DetalleVenta {
  id: number
  producto: number
  producto_nombre: string
  cantidad: number
  precio_unitario: string
  subtotal: number
}

export interface Venta {
  id: number
  mesero: number
  mesero_nombre: string
  fecha: string
  tipo: 'mesa' | 'llevar'
  mesa: number | null
  total: string
  estado: 'pedido' | 'entregado' | 'pagado' | 'cancelado'
  detalles: DetalleVenta[]
}

// Lo que el carrito guarda en memoria ANTES de enviarlo a la API
// (más simple que un DetalleVenta completo, solo lo necesario)
export interface ItemCarrito {
  producto: Producto
  cantidad: number
}
