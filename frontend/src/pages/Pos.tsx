// Pantalla principal del POS: lista de productos + carrito + cobro.
// Ver mini-clases: 08 (componentes), 09 (useState/useEffect), 10 (axios)

import { useState, useEffect } from 'react'
import api from '../api/client'
import { Header } from '../components/Header'
import { ProductoCard } from '../components/ProductoCard'
import type { Producto, ItemCarrito } from '../types'

export function Pos() {
  const [productos, setProductos] = useState<Producto[]>([])
  const [carrito, setCarrito] = useState<ItemCarrito[]>([])
  const [mensaje, setMensaje] = useState('')

  // Se ejecuta UNA vez al entrar a la pantalla: pide el menú a la API.
  useEffect(() => {
    api.get<Producto[]>('/productos/').then((res) => setProductos(res.data))
  }, [])

  function agregarAlCarrito(producto: Producto) {
    setCarrito((actual) => {
      const existente = actual.find((item) => item.producto.id === producto.id)
      if (existente) {
        // Ya está en el carrito: solo sube la cantidad (nunca mutar el array directo)
        return actual.map((item) =>
          item.producto.id === producto.id
            ? { ...item, cantidad: item.cantidad + 1 }
            : item
        )
      }
      return [...actual, { producto, cantidad: 1 }]
    })
  }

  function quitarDelCarrito(productoId: number) {
    setCarrito((actual) => actual.filter((item) => item.producto.id !== productoId))
  }

  const total = carrito.reduce(
    (acumulado, item) => acumulado + Number(item.producto.precio) * item.cantidad,
    0
  )

  async function cobrar() {
    if (carrito.length === 0) return
    setMensaje('')
    try {
      // El backend recalcula precio_unitario y total desde el servidor
      // (ver sales/serializers.py) — el frontend solo manda producto+cantidad.
      await api.post('/ventas/', {
        detalles: carrito.map((item) => ({
          producto: item.producto.id,
          cantidad: item.cantidad,
        })),
      })
      setCarrito([])
      setMensaje('✅ Venta registrada con éxito')
    } catch {
      setMensaje('❌ Error al registrar la venta')
    }
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      <div className="p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Menú de productos */}
        <div className="md:col-span-2 grid grid-cols-2 sm:grid-cols-3 gap-4">
          {productos.map((producto) => (
            <ProductoCard
              key={producto.id}
              producto={producto}
              onAgregar={agregarAlCarrito}
            />
          ))}
          {productos.length === 0 && (
            <p className="text-slate-500 col-span-full">Cargando productos...</p>
          )}
        </div>

        {/* Carrito */}
        <div className="bg-white rounded-lg shadow p-4 h-fit">
          <h2 className="font-bold text-lg mb-4">🧾 Pedido actual</h2>

          {carrito.length === 0 && (
            <p className="text-slate-400 text-sm">Toca un producto para agregarlo</p>
          )}

          <ul className="flex flex-col gap-2">
            {carrito.map((item) => (
              <li
                key={item.producto.id}
                className="flex justify-between items-center text-sm"
              >
                <span>
                  {item.cantidad}x {item.producto.nombre}
                </span>
                <button
                  onClick={() => quitarDelCarrito(item.producto.id)}
                  className="text-red-500 hover:underline"
                >
                  quitar
                </button>
              </li>
            ))}
          </ul>

          <div className="mt-4 pt-4 border-t flex justify-between font-bold">
            <span>Total</span>
            <span>${total.toLocaleString('es-CO')}</span>
          </div>

          <button
            onClick={cobrar}
            disabled={carrito.length === 0}
            className="mt-4 w-full bg-green-600 text-white py-2 rounded hover:bg-green-700 disabled:opacity-50"
          >
            Cobrar
          </button>

          {mensaje && <p className="mt-3 text-sm">{mensaje}</p>}
        </div>
      </div>
    </div>
  )
}
