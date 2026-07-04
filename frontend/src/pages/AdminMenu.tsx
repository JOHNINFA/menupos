// Gestión del menú: crear/editar/borrar categorías y productos.
// Solo accesible para usuarios con rol='admin' (ver RutaAdmin en App.tsx).

import { useState, useEffect, type FormEvent } from 'react'
import api from '../api/client'
import { Header } from '../components/Header'
import type { Categoria, Producto } from '../types'

export function AdminMenu() {
  const [categorias, setCategorias] = useState<Categoria[]>([])
  const [productos, setProductos] = useState<Producto[]>([])

  // --- Formulario de nueva categoría ---
  const [nombreCategoria, setNombreCategoria] = useState('')

  // --- Formulario de nuevo producto ---
  const [nombre, setNombre] = useState('')
  const [descripcion, setDescripcion] = useState('')
  const [precio, setPrecio] = useState('')
  const [categoriaId, setCategoriaId] = useState('')
  const [imagen, setImagen] = useState<File | null>(null)
  const [mensaje, setMensaje] = useState('')

  function cargarDatos() {
    api.get<Categoria[]>('/categorias/').then((res) => setCategorias(res.data))
    api.get<Producto[]>('/productos/').then((res) => setProductos(res.data))
  }

  useEffect(cargarDatos, [])

  async function crearCategoria(e: FormEvent) {
    e.preventDefault()
    await api.post('/categorias/', { nombre: nombreCategoria })
    setNombreCategoria('')
    cargarDatos()
  }

  async function borrarCategoria(id: number) {
    await api.delete(`/categorias/${id}/`)
    cargarDatos()
  }

  async function crearProducto(e: FormEvent) {
    e.preventDefault()
    setMensaje('')

    // Cuando hay que enviar un archivo (imagen), no se puede mandar JSON
    // normal: se usa FormData (multipart/form-data), que es como los
    // formularios HTML tradicionales suben archivos.
    const formData = new FormData()
    formData.append('nombre', nombre)
    formData.append('descripcion', descripcion)
    formData.append('precio', precio)
    formData.append('categoria', categoriaId)
    if (imagen) formData.append('imagen', imagen)

    try {
      // Al pasar un FormData, el cliente detecta que es multipart y deja
      // que el navegador ponga el Content-Type correcto automáticamente.
      await api.post('/productos/', formData)
      setNombre('')
      setDescripcion('')
      setPrecio('')
      setCategoriaId('')
      setImagen(null)
      setMensaje('✅ Producto creado')
      cargarDatos()
    } catch {
      setMensaje('❌ Revisa los datos del producto')
    }
  }

  async function alternarDisponible(producto: Producto) {
    // PATCH: editar SOLO el campo que cambió, no todo el producto.
    await api.patch(`/productos/${producto.id}/`, {
      disponible: !producto.disponible,
    })
    cargarDatos()
  }

  async function borrarProducto(id: number) {
    await api.delete(`/productos/${id}/`)
    cargarDatos()
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      <div className="p-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* --- Categorías --- */}
        <div className="bg-white rounded-lg shadow p-4">
          <h2 className="font-bold text-lg mb-4">📂 Categorías</h2>

          <form onSubmit={crearCategoria} className="flex gap-2 mb-4">
            <input
              value={nombreCategoria}
              onChange={(e) => setNombreCategoria(e.target.value)}
              placeholder="Nueva categoría"
              className="flex-1 border rounded px-3 py-2"
              required
            />
            <button className="bg-orange-600 text-white px-4 rounded hover:bg-orange-700">
              Agregar
            </button>
          </form>

          <ul className="flex flex-col gap-2">
            {categorias.map((cat) => (
              <li key={cat.id} className="flex justify-between items-center text-sm border-b pb-1">
                {cat.nombre}
                <button
                  onClick={() => borrarCategoria(cat.id)}
                  className="text-red-500 hover:underline"
                >
                  borrar
                </button>
              </li>
            ))}
          </ul>
        </div>

        {/* --- Nuevo producto --- */}
        <div className="bg-white rounded-lg shadow p-4">
          <h2 className="font-bold text-lg mb-4">🍔 Nuevo producto</h2>

          <form onSubmit={crearProducto} className="flex flex-col gap-3">
            <input
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              placeholder="Nombre"
              className="border rounded px-3 py-2"
              required
            />
            <textarea
              value={descripcion}
              onChange={(e) => setDescripcion(e.target.value)}
              placeholder="Descripción (opcional)"
              className="border rounded px-3 py-2"
            />
            <input
              type="number"
              step="0.01"
              value={precio}
              onChange={(e) => setPrecio(e.target.value)}
              placeholder="Precio"
              className="border rounded px-3 py-2"
              required
            />
            <select
              value={categoriaId}
              onChange={(e) => setCategoriaId(e.target.value)}
              className="border rounded px-3 py-2"
              required
            >
              <option value="">-- Selecciona categoría --</option>
              {categorias.map((cat) => (
                <option key={cat.id} value={cat.id}>
                  {cat.nombre}
                </option>
              ))}
            </select>
            <input
              type="file"
              accept="image/*"
              onChange={(e) => setImagen(e.target.files?.[0] ?? null)}
            />
            <button className="bg-green-600 text-white py-2 rounded hover:bg-green-700">
              Crear producto
            </button>
            {mensaje && <p className="text-sm">{mensaje}</p>}
          </form>
        </div>

        {/* --- Lista de productos --- */}
        <div className="bg-white rounded-lg shadow p-4 lg:col-span-2">
          <h2 className="font-bold text-lg mb-4">📋 Productos existentes</h2>

          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
            {productos.map((producto) => (
              <div key={producto.id} className="border rounded-lg p-3 text-sm">
                <p className="font-semibold">{producto.nombre}</p>
                <p className="text-slate-500">{producto.categoria_nombre}</p>
                <p className="font-bold text-orange-600">
                  ${Number(producto.precio).toLocaleString('es-CO')}
                </p>
                <div className="flex justify-between mt-2">
                  <button
                    onClick={() => alternarDisponible(producto)}
                    className={producto.disponible ? 'text-green-600' : 'text-slate-400'}
                  >
                    {producto.disponible ? '✅ Disponible' : '🚫 Oculto'}
                  </button>
                  <button
                    onClick={() => borrarProducto(producto.id)}
                    className="text-red-500 hover:underline"
                  >
                    borrar
                  </button>
                </div>
              </div>
            ))}
          </div>

          {productos.length === 0 && (
            <p className="text-slate-400 text-sm">Aún no hay productos creados.</p>
          )}
        </div>
      </div>
    </div>
  )
}
