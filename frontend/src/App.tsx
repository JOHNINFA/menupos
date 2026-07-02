// App.tsx = el componente RAÍZ de React (el "punto de entrada" visual).
// Todo lo que ves en pantalla nace desde aquí.
//
// Por ahora es solo una pantalla de bienvenida para confirmar que
// Vite + React + Tailwind están funcionando juntos correctamente.
// En FASE 6 esto se reemplaza por el router real (login, dashboard, POS).

function App() {
  return (
    // Clases de Tailwind: min-h-screen (altura completa), flex+center
    // (centrar contenido), bg-slate-900 (fondo oscuro), text-white (texto blanco)
    <div className="min-h-screen flex flex-col items-center justify-center bg-slate-900 text-white gap-4">
      <h1 className="text-4xl font-bold">🍔 MenuPOS</h1>
      <p className="text-slate-400">
        Frontend conectado: React + Vite + TypeScript + Tailwind CSS
      </p>
      <p className="text-sm text-slate-500">FASE 3 completada ✅</p>
    </div>
  )
}

export default App
