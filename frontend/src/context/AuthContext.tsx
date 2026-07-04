// Contexto de autenticación. Ver mini-clase:
// docs/clases/10-consumir-api.md (sección "Context API")

import { createContext, useContext, useState, useEffect } from 'react'
import type { ReactNode } from 'react'
import api from '../api/client'
import type { Usuario } from '../types'

interface AuthContextType {
  user: Usuario | null
  login: (username: string, password: string) => Promise<void>
  logout: () => void
  loading: boolean
}

const AuthContext = createContext<AuthContextType | null>(null)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<Usuario | null>(null)
  // loading = "todavía no sabemos si hay sesión activa". Evita que la app
  // parpadee mostrando el login antes de confirmar un token guardado.
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Al abrir la app, si hay un token guardado de una sesión anterior,
    // preguntamos a la API quién es ese usuario (endpoint /users/me/).
    const token = localStorage.getItem('access')
    if (!token) {
      setLoading(false)
      return
    }

    api
      .get<Usuario>('/users/me/')
      .then((res) => setUser(res.data))
      .catch(() => {
        // Token vencido o inválido: limpiamos todo y que vuelva a loguearse
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
      })
      .finally(() => setLoading(false))
  }, [])

  async function login(username: string, password: string) {
    const res = await api.post<{ access: string; refresh: string }>(
      '/auth/login/',
      { username, password }
    )
    localStorage.setItem('access', res.data.access)
    localStorage.setItem('refresh', res.data.refresh)

    const me = await api.get<Usuario>('/users/me/')
    setUser(me.data)
  }

  function logout() {
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  )
}

// Hook para consumir el contexto fácilmente: useAuth() en vez de
// useContext(AuthContext) en cada componente.
export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth debe usarse dentro de un <AuthProvider>')
  }
  return context
}
