// Gestión de usuarios (meseros/admins). Solo accesible para rol='admin'
// (ver RutaAdmin en App.tsx). El backend también lo protege (EsAdmin).

import { useState, useEffect, type FormEvent } from 'react'
import api from '../api/client'
import { Header } from '../components/Header'
import type { Usuario } from '../types'

export function AdminUsuarios() {
  const [usuarios, setUsuarios] = useState<Usuario[]>([])
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [rol, setRol] = useState<'mesero' | 'admin'>('mesero')
  const [mensaje, setMensaje] = useState('')

  function cargarUsuarios() {
    api.get<Usuario[]>('/usuarios/').then((res) => setUsuarios(res.data))
  }

  useEffect(cargarUsuarios, [])

  async function crearUsuario(e: FormEvent) {
    e.preventDefault()
    setMensaje('')
    try {
      await api.post('/usuarios/', { username, password, rol })
      setUsername('')
      setPassword('')
      setRol('mesero')
      setMensaje('✅ Usuario creado')
      cargarUsuarios()
    } catch {
      setMensaje('❌ Revisa los datos (usuario repetido o contraseña muy corta)')
    }
  }

  async function borrarUsuario(id: number) {
    try {
      await api.delete(`/usuarios/${id}/`)
      cargarUsuarios()
    } catch {
      // El backend devuelve 400 con un mensaje claro si el usuario ya
      // tiene ventas registradas (on_delete=PROTECT, ver sales/models.py).
      alert('No se puede borrar: este usuario ya tiene ventas registradas.')
    }
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      <div className="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-4">
          <h2 className="font-bold text-lg mb-4">➕ Nuevo usuario</h2>
          <form onSubmit={crearUsuario} className="flex flex-col gap-3">
            <input
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Nombre de usuario"
              className="border rounded px-3 py-2"
              required
            />
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Contraseña (mín. 6 caracteres)"
              className="border rounded px-3 py-2"
              minLength={6}
              required
            />
            <select
              value={rol}
              onChange={(e) => setRol(e.target.value as 'mesero' | 'admin')}
              className="border rounded px-3 py-2"
            >
              <option value="mesero">Mesero</option>
              <option value="admin">Administrador</option>
            </select>
            <button className="bg-orange-600 text-white py-2 rounded hover:bg-orange-700">
              Crear usuario
            </button>
            {mensaje && <p className="text-sm">{mensaje}</p>}
          </form>
        </div>

        <div className="bg-white rounded-lg shadow p-4">
          <h2 className="font-bold text-lg mb-4">👥 Usuarios existentes</h2>
          <ul className="flex flex-col gap-2">
            {usuarios.map((u) => (
              <li key={u.id} className="flex justify-between items-center text-sm border-b pb-1">
                <span>
                  {u.username} <span className="text-slate-400">({u.rol})</span>
                </span>
                <button
                  onClick={() => borrarUsuario(u.id)}
                  className="text-red-500 hover:underline"
                >
                  borrar
                </button>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  )
}
