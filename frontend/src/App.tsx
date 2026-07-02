// Punto de entrada visual: define las rutas de la app y envuelve todo
// con el AuthProvider para que cualquier pantalla sepa quién está logueado.

import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'
import { RutaProtegida } from './components/RutaProtegida'
import { Login } from './pages/Login'
import { Pos } from './pages/Pos'
import { Dashboard } from './pages/Dashboard'

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />

          <Route
            path="/pos"
            element={
              <RutaProtegida>
                <Pos />
              </RutaProtegida>
            }
          />

          <Route
            path="/dashboard"
            element={
              <RutaProtegida>
                <Dashboard />
              </RutaProtegida>
            }
          />

          {/* Cualquier otra ruta redirige al POS (que a su vez redirige
              a /login si no hay sesión activa) */}
          <Route path="*" element={<Navigate to="/pos" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  )
}

export default App
