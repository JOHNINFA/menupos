// Barra superior con navegación y botón de logout.
// Componente reutilizable: se usa en Pos.tsx y Dashboard.tsx.

import { Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

export function Header() {
  const { user, logout } = useAuth()

  return (
    <header className="flex items-center justify-between px-6 py-4 bg-slate-800 text-white">
      <div className="flex items-center gap-6">
        <span className="font-bold text-lg">🍔 MenuPOS</span>
        <Link to="/pos" className="hover:text-orange-400">
          Punto de Venta
        </Link>
        <Link to="/dashboard" className="hover:text-orange-400">
          Dashboard
        </Link>
        {/* Solo el admin ve estos enlaces de gestión */}
        {user?.rol === 'admin' && (
          <>
            <Link to="/menu" className="hover:text-orange-400">
              Gestión de Menú
            </Link>
            <Link to="/usuarios" className="hover:text-orange-400">
              Usuarios
            </Link>
          </>
        )}
      </div>
      <div className="flex items-center gap-4 text-sm">
        <span>
          {user?.username} ({user?.rol})
        </span>
        <button
          onClick={logout}
          className="px-3 py-1 rounded bg-red-600 hover:bg-red-700"
        >
          Salir
        </button>
      </div>
    </header>
  )
}
