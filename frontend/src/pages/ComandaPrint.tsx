// Vista imprimible de una venta (la "comanda" que iría a cocina/caja).
// Se abre desde el Dashboard. El botón Imprimir usa window.print(),
// que respeta las clases `print:hidden` de Tailwind para ocultar
// todo lo que no debe salir en el papel (header, botones).

import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import api from '../api/client'
import type { Venta } from '../types'

export function ComandaPrint() {
  const { id } = useParams()
  const navigate = useNavigate()
  const [venta, setVenta] = useState<Venta | null>(null)

  useEffect(() => {
    api.get<Venta>(`/ventas/${id}/`).then((res) => setVenta(res.data))
  }, [id])

  if (!venta) {
    return <div className="p-6">Cargando comanda...</div>
  }

  return (
    <div className="min-h-screen bg-slate-100 flex flex-col items-center py-8">
      {/* print:hidden = esto NO aparece al imprimir (Ctrl+P) */}
      <div className="print:hidden mb-4 flex gap-2">
        <button
          onClick={() => window.print()}
          className="bg-orange-600 text-white px-4 py-2 rounded hover:bg-orange-700"
        >
          🖨️ Imprimir
        </button>
        <button
          onClick={() => navigate(-1)}
          className="bg-slate-300 px-4 py-2 rounded hover:bg-slate-400"
        >
          Volver
        </button>
      </div>

      {/* Esta tarjeta SÍ se imprime: formato angosto tipo ticket */}
      <div className="bg-white shadow p-6 w-80 font-mono text-sm">
        <h1 className="text-center font-bold text-lg mb-2">🍔 MenuPOS</h1>
        <p className="text-center text-xs mb-4">Comanda de pedido</p>

        <div className="border-t border-dashed pt-2 mb-2">
          <p>
            {venta.tipo === 'mesa' ? (
              <>Mesa: <strong>{venta.mesa}</strong></>
            ) : (
              <strong>Para llevar</strong>
            )}
          </p>
          <p>Mesero: {venta.mesero_nombre}</p>
          <p>Fecha: {new Date(venta.fecha).toLocaleString('es-CO')}</p>
          <p>Estado: {venta.estado}</p>
        </div>

        <div className="border-t border-dashed pt-2 mb-2">
          {venta.detalles.map((d) => (
            <div key={d.id} className="flex justify-between">
              <span>{d.cantidad}x {d.producto_nombre}</span>
              <span>${Number(d.subtotal).toLocaleString('es-CO')}</span>
            </div>
          ))}
        </div>

        <div className="border-t border-dashed pt-2 flex justify-between font-bold">
          <span>TOTAL</span>
          <span>${Number(venta.total).toLocaleString('es-CO')}</span>
        </div>
      </div>
    </div>
  )
}
