// Historial de ventas: lista consumiendo GET /api/ventas/, con acciones
// de cajero (marcar pagada/cancelada) y acceso a la comanda imprimible.

import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../api/client'
import { Header } from '../components/Header'
import { useAuth } from '../context/AuthContext'
import type { Venta } from '../types'

// Color de cada estado del flujo (pedido → entregado → pagado / cancelado)
const ESTILO_ESTADO: Record<Venta['estado'], string> = {
  pedido: 'bg-yellow-100 text-yellow-800',
  entregado: 'bg-blue-100 text-blue-800',
  pagado: 'bg-green-100 text-green-800',
  cancelado: 'bg-red-100 text-red-800',
}

export function Dashboard() {
  const { user } = useAuth()
  const [ventas, setVentas] = useState<Venta[]>([])

  function cargarVentas() {
    api.get<Venta[]>('/ventas/').then((res) => setVentas(res.data))
  }

  useEffect(cargarVentas, [])

  // El "total cobrado" solo cuenta lo que realmente se pagó.
  const totalCobrado = ventas
    .filter((v) => v.estado === 'pagado')
    .reduce((acc, v) => acc + Number(v.total), 0)

  // Cuentas abiertas = aún no pagadas ni canceladas (pedido o entregado).
  const abiertas = ventas.filter(
    (v) => v.estado === 'pedido' || v.estado === 'entregado'
  ).length

  async function marcarEstado(
    id: number,
    estado: 'entregado' | 'pagado' | 'cancelado'
  ) {
    // Endpoint dedicado (no un PATCH genérico): ver sales/views.py
    await api.post(`/ventas/${id}/marcar_estado/`, { estado })
    cargarVentas()
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      <div className="p-6">
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mb-6">
          <div className="bg-white rounded-lg shadow p-4">
            <p className="text-sm text-slate-500">Cuentas abiertas</p>
            <p className="text-2xl font-bold">{abiertas}</p>
          </div>
          <div className="bg-white rounded-lg shadow p-4">
            <p className="text-sm text-slate-500">Total cobrado</p>
            <p className="text-2xl font-bold">${totalCobrado.toLocaleString('es-CO')}</p>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow overflow-hidden">
          <table className="w-full text-sm">
            <thead className="bg-slate-800 text-white">
              <tr>
                <th className="p-3 text-left">#</th>
                <th className="p-3 text-left">Ubicación</th>
                <th className="p-3 text-left">Mesero</th>
                <th className="p-3 text-left">Fecha</th>
                <th className="p-3 text-left">Productos</th>
                <th className="p-3 text-right">Total</th>
                <th className="p-3 text-left">Estado</th>
                <th className="p-3 text-left">Acciones</th>
              </tr>
            </thead>
            <tbody>
              {ventas.map((venta) => (
                <tr key={venta.id} className="border-t">
                  <td className="p-3">#{venta.id}</td>
                  <td className="p-3">
                    {venta.tipo === 'mesa' ? `Mesa ${venta.mesa}` : '🥡 Para llevar'}
                  </td>
                  <td className="p-3">{venta.mesero_nombre}</td>
                  <td className="p-3">
                    {new Date(venta.fecha).toLocaleString('es-CO')}
                  </td>
                  <td className="p-3">
                    {venta.detalles
                      .map((d) => `${d.cantidad}x ${d.producto_nombre}`)
                      .join(', ')}
                  </td>
                  <td className="p-3 text-right">
                    ${Number(venta.total).toLocaleString('es-CO')}
                  </td>
                  <td className="p-3">
                    <span className={`px-2 py-1 rounded text-xs capitalize ${ESTILO_ESTADO[venta.estado]}`}>
                      {venta.estado}
                    </span>
                  </td>
                  <td className="p-3">
                    <div className="flex gap-2 items-center flex-wrap">
                      <Link
                        to={`/comanda/${venta.id}`}
                        className="text-blue-600 hover:underline text-xs"
                      >
                        Ver comanda
                      </Link>

                      {/* El mesero (o admin) marca ENTREGADO cuando lleva
                          los platos a la mesa: solo tiene sentido si el
                          pedido está en estado 'pedido'. */}
                      {venta.estado === 'pedido' && (
                        <button
                          onClick={() => marcarEstado(venta.id, 'entregado')}
                          className="text-blue-600 hover:underline text-xs"
                        >
                          Marcar entregado
                        </button>
                      )}

                      {/* Solo el admin/cajero cobra o cancela, y solo
                          mientras la cuenta siga abierta (no pagada). */}
                      {user?.rol === 'admin' &&
                        (venta.estado === 'pedido' || venta.estado === 'entregado') && (
                          <>
                            <button
                              onClick={() => marcarEstado(venta.id, 'pagado')}
                              className="text-green-600 hover:underline text-xs"
                            >
                              Cobrar
                            </button>
                            <button
                              onClick={() => marcarEstado(venta.id, 'cancelado')}
                              className="text-red-600 hover:underline text-xs"
                            >
                              Cancelar
                            </button>
                          </>
                        )}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {ventas.length === 0 && (
            <p className="p-4 text-slate-400 text-sm">Aún no hay ventas registradas.</p>
          )}
        </div>
      </div>
    </div>
  )
}
