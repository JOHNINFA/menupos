// Historial de ventas: lista simple consumiendo GET /api/ventas/

import { useState, useEffect } from 'react'
import api from '../api/client'
import { Header } from '../components/Header'
import type { Venta } from '../types'

export function Dashboard() {
  const [ventas, setVentas] = useState<Venta[]>([])

  useEffect(() => {
    api.get<Venta[]>('/ventas/').then((res) => setVentas(res.data))
  }, [])

  const totalDelDia = ventas.reduce((acc, v) => acc + Number(v.total), 0)

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      <div className="p-6">
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mb-6">
          <div className="bg-white rounded-lg shadow p-4">
            <p className="text-sm text-slate-500">Ventas registradas</p>
            <p className="text-2xl font-bold">{ventas.length}</p>
          </div>
          <div className="bg-white rounded-lg shadow p-4">
            <p className="text-sm text-slate-500">Total acumulado</p>
            <p className="text-2xl font-bold">${totalDelDia.toLocaleString('es-CO')}</p>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow overflow-hidden">
          <table className="w-full text-sm">
            <thead className="bg-slate-800 text-white">
              <tr>
                <th className="p-3 text-left">#</th>
                <th className="p-3 text-left">Mesero</th>
                <th className="p-3 text-left">Fecha</th>
                <th className="p-3 text-left">Productos</th>
                <th className="p-3 text-right">Total</th>
                <th className="p-3 text-left">Estado</th>
              </tr>
            </thead>
            <tbody>
              {ventas.map((venta) => (
                <tr key={venta.id} className="border-t">
                  <td className="p-3">#{venta.id}</td>
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
                  <td className="p-3 capitalize">{venta.estado}</td>
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
