import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// Configuración de Vite: el "motor" que compila y sirve el frontend
// en desarrollo (recuerda: Vite = por qué React arranca rápido).
// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),        // Soporte para JSX/TSX de React
    tailwindcss(),  // Tailwind CSS v4 se integra como plugin de Vite (sin config.js)
  ],
  server: {
    port: 5173, // Puerto fijo (coincide con CORS_ALLOWED_ORIGINS del backend)
  },
})
