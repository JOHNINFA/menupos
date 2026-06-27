# 📊 Diagrama 01 — Visión general de MenuPOS

> 🎯 **Para qué sirve**: ver de un vistazo cómo está armado todo MenuPOS y cómo fluye la información.
> 📖 **Clase asociada**: [`../clases/01-arquitectura.md`](../clases/01-arquitectura.md)

---

## 🏗️ La arquitectura completa

Este diagrama muestra **todas las piezas** de MenuPOS y cómo se conectan.

```mermaid
flowchart TB
    subgraph FRONT["🎨 FRONTEND (Salón del restaurante)"]
        A[👨‍💼 Mesero usa<br/>navegador Chrome]
        B[React + Vite<br/>+ Tailwind]
        A --> B
    end

    subgraph API["🌐 INTERNET / API REST"]
        C{Verbos HTTP<br/>GET POST PUT DELETE}
        D[Mensajes en<br/>formato JSON]
    end

    subgraph BACK["⚙️ BACKEND (Cocina del restaurante)"]
        E[Django + DRF<br/>en Railway]
        F[(PostgreSQL<br/>Base de datos)]
        G[(AWS S3<br/>Imágenes)]
        E --> F
        E --> G
    end

    B <--> C
    C <--> D
    D <--> E

    style FRONT fill:#dbeafe,stroke:#3b82f6,color:#000
    style API fill:#fef3c7,stroke:#f59e0b,color:#000
    style BACK fill:#dcfce7,stroke:#22c55e,color:#000
```

> 💡 **Tip**: En GitHub este diagrama se ve renderizado automáticamente como imagen.

---

## 🔄 Flujo de una petición típica

Imaginemos que el mesero abre la lista de productos:

```mermaid
sequenceDiagram
    autonumber
    participant U as 👨‍💼 Mesero<br/>(Frontend)
    participant A as 🌐 API REST<br/>(/api/productos/)
    participant D as 🍳 Django<br/>(Backend)
    participant P as 💾 PostgreSQL<br/>(Base de datos)

    U->>A: GET /api/productos/
    A->>D: ¿Cuáles productos hay?
    D->>P: SELECT * FROM productos
    P-->>D: [hamburguesa, pizza, jugo, ...]
    D->>D: Convierte a JSON
    D-->>A: 200 OK + JSON
    A-->>U: Lista de productos
    Note over U: Pinta los productos<br/>en pantalla 🎨
```

---

## 🗂️ Capas del backend (cómo Django organiza la cocina)

Esto es **lo que está dentro del backend** específicamente:

```mermaid
flowchart LR
    REQ[Petición HTTP<br/>desde frontend]

    subgraph DJANGO["⚙️ Django Backend"]
        URL[URL<br/>'/api/productos/']
        VIEW[ViewSet<br/>'Comedor']
        SER[Serializer<br/>'Mesero traductor']
        MOD[Modelo<br/>'Receta']
    end

    DB[(PostgreSQL<br/>'Refrigerador')]
    RES[Respuesta JSON<br/>al frontend]

    REQ --> URL
    URL --> VIEW
    VIEW --> SER
    SER --> MOD
    MOD <--> DB
    SER --> RES

    style DJANGO fill:#dcfce7,stroke:#22c55e,color:#000
    style DB fill:#fde68a,stroke:#f59e0b,color:#000
    style REQ fill:#dbeafe,stroke:#3b82f6,color:#000
    style RES fill:#dbeafe,stroke:#3b82f6,color:#000
```

### ¿Qué hace cada pieza?

| Pieza | Rol en el restaurante | Qué hace técnicamente |
|---|---|---|
| **URL** | 🚪 Puerta del comedor | Decide a qué función llevar la petición |
| **ViewSet** | 🍽️ Comedor | Recibe la petición, decide qué hacer |
| **Serializer** | 🧑‍💼 Mesero traductor | Convierte entre objetos Python y JSON |
| **Modelo** | 📖 Receta | Define cómo se ve un dato en la BD |
| **PostgreSQL** | ❄️ Refrigerador | Guarda todos los datos físicamente |

> 📚 Cada una de estas piezas tendrá su propia mini-clase cuando llegue su momento.

---

## 🎯 Cómo usar este diagrama en una entrevista

Cuando te pregunten "¿cómo está armado tu proyecto?":

1. Abre este archivo en GitHub
2. Muestra el primer diagrama (visión general)
3. Explica: "Tengo un frontend en React que llama a una API REST construida en Django, que guarda datos en PostgreSQL y las imágenes en AWS S3"
4. Si quieren más detalle, abre el diagrama de capas del backend
5. Explica cada pieza usando la metáfora del restaurante

**Pum**. Te ven como un dev que **entiende** lo que construyó.

---

## 🔗 Diagramas relacionados (próximamente)

- `02-modelo-er.md` → Cómo se relacionan las tablas de la BD
- `03-flujo-autenticacion.md` → Cómo funciona el login con JWT
- `04-flujo-crear-venta.md` → Cómo se procesa una venta desde el botón "Cobrar"
