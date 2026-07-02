// Envuelve páginas que requieren login. Si no hay usuario, redirige a /login.

import type { ReactNode } from 'react'
import { Navigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

export function RutaProtegida({ children }: { children: ReactNode }) {
  const { user, loading } = useAuth()

  if (loading) {
    // Mientras verificamos si hay sesión activa, no mostramos nada
    // definitivo (evita el "parpadeo" de mostrar login y luego el POS).
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-900 text-white">
        Cargando...
      </div>
    )
  }

  if (!user) {
    return <Navigate to="/login" replace />
  }

  return <>{children}</>
}
