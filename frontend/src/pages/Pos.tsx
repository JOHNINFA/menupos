// Pantalla principal del POS: filtro por categoría + productos + orden.
// Ver mini-clases: 08 (componentes), 09 (useState/useEffect), 10 (fetch/API)

import { useState, useEffect } from 'react'
import api from '../api/client'
import { Header } from '../components/Header'
import { ProductoCard } from '../components/ProductoCard'
import type { Producto, Categoria, ItemCarrito } from '../types'

export function Pos() {
  const [productos, setProductos] = useState<Producto[]>([])
  const [categorias, setCategorias] = useState<Categoria[]>([])
  const [categoriaActiva, setCategoriaActiva] = useState<number | null>(null)
  const [carrito, setCarrito] = useState<ItemCarrito[]>([])
  const [tipo, setTipo] = useState<'mesa' | 'llevar'>('mesa')
  const [mesa, setMesa] = useState('')
  const [mensaje, setMensaje] = useState('')

  // Al entrar: pedimos productos y categorías a la API.
  useEffect(() => {
    api.get<Producto[]>('/productos/').then((res) => setProductos(res.data))
    api.get<Categoria[]>('/categorias/').then((res) => setCategorias(res.data))
  }, [])

  // Productos visibles: solo disponibles y de la categoría seleccionada.
  const productosVisibles = productos.filter(
    (p) =>
      p.disponible &&
      (categoriaActiva === null || p.categoria === categoriaActiva)
  )

  function agregarAlCarrito(producto: Producto) {
    setCarrito((actual) => {
      const existente = actual.find((item) => item.producto.id === producto.id)
      if (existente) {
        return actual.map((item) =>
          item.producto.id === producto.id
            ? { ...item, cantidad: item.cantidad + 1 }
            : item
        )
      }
      return [...actual, { producto, cantidad: 1 }]
    })
  }

  // Sube o baja la cantidad de un item; si llega a 0, lo saca del pedido.
  function cambiarCantidad(productoId: number, delta: number) {
    setCarrito((actual) =>
      actual.flatMap((item) => {
        if (item.producto.id !== productoId) return [item]
        const nueva = item.cantidad + delta
        return nueva <= 0 ? [] : [{ ...item, cantidad: nueva }]
      })
    )
  }

  const total = carrito.reduce(
    (acc, item) => acc + Number(item.producto.precio) * item.cantidad,
    0
  )

  const faltaMesa = tipo === 'mesa' && !mesa

  async function enviarPedido() {
    if (carrito.length === 0 || faltaMesa) return
    setMensaje('')
    try {
      await api.post('/ventas/', {
        tipo,
        mesa: tipo === 'mesa' ? Number(mesa) : null,
        detalles: carrito.map((item) => ({
          producto: item.producto.id,
          cantidad: item.cantidad,
        })),
      })
      setCarrito([])
      setMesa('')
      setMensaje(
        tipo === 'mesa'
          ? `✅ Pedido enviado a la mesa ${mesa}`
          : '✅ Pedido para llevar enviado'
      )
    } catch {
      setMensaje('❌ Error al registrar el pedido')
    }
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      <div className="p-4 md:p-6 grid grid-cols-1 lg:grid-cols-3 gap-6 items-start">
        {/* ===== Columna izquierda: categorías + productos ===== */}
        <div className="lg:col-span-2">
          {/* Tabs de categorías (pills) */}
          <div className="flex flex-wrap gap-2 mb-4">
            <button
              onClick={() => setCategoriaActiva(null)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium transition-colors ${
                categoriaActiva === null
                  ? 'bg-slate-800 text-white'
                  : 'bg-white text-slate-600 hover:bg-slate-200'
              }`}
            >
              Todos
            </button>
            {categorias.map((cat) => (
              <button
                key={cat.id}
                onClick={() => setCategoriaActiva(cat.id)}
                className={`px-4 py-1.5 rounded-full text-sm font-medium transition-colors ${
                  categoriaActiva === cat.id
                    ? 'bg-slate-800 text-white'
                    : 'bg-white text-slate-600 hover:bg-slate-200'
                }`}
              >
                {cat.nombre}
              </button>
            ))}
          </div>

          {/* Grid de productos */}
          <div className="grid grid-cols-2 sm:grid-cols-3 xl:grid-cols-4 gap-3 items-start">
            {productosVisibles.map((producto) => (
              <ProductoCard
                key={producto.id}
                producto={producto}
                onAgregar={agregarAlCarrito}
              />
            ))}
          </div>

          {productos.length === 0 && (
            <p className="text-slate-500">Cargando productos...</p>
          )}
          {productos.length > 0 && productosVisibles.length === 0 && (
            <p className="text-slate-400 text-sm">No hay productos en esta categoría.</p>
          )}
        </div>

        {/* ===== Columna derecha: resumen del pedido ===== */}
        <div className="bg-white rounded-2xl shadow-sm p-5 lg:sticky lg:top-6">
          <div className="flex items-center gap-2 mb-1">
            <span className="text-xl">🧾</span>
            <h2 className="font-bold text-lg text-slate-800">Pedido actual</h2>
          </div>
          <p className="text-xs text-slate-400 uppercase tracking-wide mb-4">
            Resumen de orden
          </p>

          {/* Tipo de pedido */}
          <div className="flex gap-2 mb-3">
            <button
              type="button"
              onClick={() => setTipo('mesa')}
              className={`flex-1 py-2 rounded-lg text-sm font-medium ${
                tipo === 'mesa' ? 'bg-orange-500 text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              🍽️ Mesa
            </button>
            <button
              type="button"
              onClick={() => setTipo('llevar')}
              className={`flex-1 py-2 rounded-lg text-sm font-medium ${
                tipo === 'llevar' ? 'bg-orange-500 text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              🥡 Para llevar
            </button>
          </div>

          {tipo === 'mesa' && (
            <div className="mb-4">
              <label className="block text-sm text-slate-600 mb-1">Número de mesa</label>
              <input
                type="number"
                min={1}
                value={mesa}
                onChange={(e) => setMesa(e.target.value)}
                placeholder="Ej: 5"
                className="w-full border border-slate-200 rounded-lg px-3 py-2"
              />
            </div>
          )}

          {/* Items del pedido */}
          {carrito.length === 0 ? (
            <div className="text-center py-8 text-slate-400">
              <div className="text-4xl mb-2">🛒</div>
              <p className="text-sm">Toca un producto para agregarlo</p>
              <p className="text-xs">Aún no hay platos en la orden</p>
            </div>
          ) : (
            <ul className="flex flex-col gap-3 mb-4">
              {carrito.map((item) => (
                <li key={item.producto.id} className="flex items-center gap-2">
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-slate-800 truncate">
                      {item.producto.nombre}
                    </p>
                    <p className="text-xs text-slate-400">
                      ${Number(item.producto.precio).toLocaleString('es-CO')} c/u
                    </p>
                  </div>
                  {/* Controles de cantidad */}
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => cambiarCantidad(item.producto.id, -1)}
                      className="w-6 h-6 rounded-full bg-slate-100 text-slate-600 hover:bg-slate-200"
                    >
                      −
                    </button>
                    <span className="w-5 text-center text-sm font-semibold">
                      {item.cantidad}
                    </span>
                    <button
                      onClick={() => cambiarCantidad(item.producto.id, 1)}
                      className="w-6 h-6 rounded-full bg-slate-100 text-slate-600 hover:bg-slate-200"
                    >
                      +
                    </button>
                  </div>
                </li>
              ))}
            </ul>
          )}

          {/* Total */}
          <div className="pt-4 border-t flex justify-between items-center mb-4">
            <span className="font-semibold text-slate-800">Total</span>
            <span className="font-bold text-xl text-orange-600">
              ${total.toLocaleString('es-CO')}
            </span>
          </div>

          <button
            onClick={enviarPedido}
            disabled={carrito.length === 0 || faltaMesa}
            className="w-full bg-green-500 text-white py-3 rounded-xl font-semibold hover:bg-green-600 disabled:opacity-50 transition-colors"
          >
            ▷ Enviar pedido
          </button>

          {carrito.length > 0 && (
            <button
              onClick={() => setCarrito([])}
              className="w-full mt-2 text-slate-400 text-xs uppercase tracking-wide hover:text-slate-600"
            >
              Limpiar pedido
            </button>
          )}

          {mensaje && <p className="mt-3 text-sm text-center">{mensaje}</p>}
        </div>
      </div>
    </div>
  )
}
