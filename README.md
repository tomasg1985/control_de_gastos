# 📊 Sistema de Gestión Financiera Analítico con Persistencia SQL y Auditoría TXT

Una solución analítica y robusta desarrollada en **Python** para el control y auditoría de finanzas personales. Este ecosistema implementa una arquitectura híbrida avanzada: combina la velocidad de procesamiento en memoria de estructuras de listas y diccionarios, la persistencia estructurada de un motor relacional de base de datos y un sistema secundario redundante de auditoría por archivos planos.

---

### 🚀 Innovaciones y Características Técnicas

*   **Persistencia Relacional Avanzada (SQLite):** Implementación de una base de datos embebida con esquemas normalizados e índices autoincrementales (`INTEGER PRIMARY KEY AUTOINCREMENT`) para asegurar la integridad física de las transacciones financieras.
*   **Sistema de Logs Defensivo (.txt):** Mecanismo secundario de auditoría que inyecta en caliente un registro histórico redundante cada vez que ocurre un evento de escritura, utilizando manejadores de contexto seguros (`with open()`).
*   **Sellado de Tiempo Dinámico (*Timestamping*):** Integración precisa del módulo `datetime` para registrar con exactitud cronológica (`%d/%m/%Y %H:%M`) cada uno de los movimientos económicos procesados.
*   **Motor Analítico y Estadístico Integrado:** Algoritmos optimizados para el cálculo de reportes agregados en tiempo real: promedio ponderado, sumatorias acumuladas (`sum()`), y detección de extremos financieros (picos máximos y mínimos de consumo).
*   **Sincronización de Estado Local / Disco:** Capacidad de inicialización inteligente que consulta el disco al arrancar el programa, transforma las tuplas relacionales en estructuras nativas de Python y reconstruye dinámicamente la memoria de la aplicación.

---

### 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.10+ *(Soporte de coincidencia estructural mediante match-case)*
*   **Persistencia Core:** [SQLite3](https://python.org) (Base de datos relacional integrada)
*   **Persistencia de Auditoría:** File System I/O nativo (Escritura asíncrona de archivos `.txt`)
*   **Librerías de Soporte:** `datetime` (Marcado temporal), `colorama` (Feedback UX en consola)

---

### 🗄️ Esquema de la Base de Datos Relacional

Al inicializarse, el sistema asegura la estructura del almacenamiento local creando de manera automatizada la siguiente entidad relacional:

```sql
CREATE TABLE IF NOT EXISTS historial_gastos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL,
    monto REAL NOT NULL,
    fecha TEXT NOT NULL,
    categoria TEXT NOT NULL
);
```

---

### 📂 Arquitectura del Módulo Lógico (`logica_gastos.py`)

Las reglas de negocio y mutaciones de datos del software se rigen por la siguiente API de funciones:

| Función | Tipo de Operación | Impacto Técnico |
| :--- | :--- | :--- |
| `cargar_datos_desde_db()` | **Boot / Lectura** | Extrae las tuplas del archivo `.db`, las mapea en diccionarios y genera la lista de estado principal. |
| `agregar_gasto()` | **Escritura Dual (INSERT / Append)** | Registra la operación en la DB relacional, actualiza la lista en memoria y escribe una línea de log en `historial_gastos.txt`. |
| `ver_historial()` | **Lectura Estructurada** | Itera y desestructura los diccionarios formateando los montos numéricos con precisión decimal (`:.2f`). |
| `buscar_gasto()` | **Filtro de Texto** | Algoritmo de búsqueda insensible a mayúsculas (`.lower()`) que escanea en paralelo categorías y descripciones. |
| `editar_gasto()` | **Mutación (UPDATE)** | Modifica los punteros de la lista local por índice (`.update()`) y ejecuta la actualización relacional filtrando por ID único. |
| `eliminar_gasto()` | **Destrucción (DELETE)** | Remueve el elemento de la memoria intermedia (`.pop()`) y ejecuta la sentencia física de borrado en SQLite. |
| `mostrar_reporte()` | **Análisis de Datos** | Aplica comprensiones de listas sobre los montos de la aplicación para aislar y procesar las variables estadísticas del sistema. |

---

### ⚙️ Instalación y Operación Local

Configura el sistema financiero en tu computadora ejecutando los siguientes comandos:

1. **Clonar el repositorio optimizado:**
   ```bash
   git clone https://github.com
   cd control_de_gastos
   ```

2. **Instalar el manejador de color de interfaz:**
   ```bash
   pip install colorama
   ```

3. **Iniciar el programa principal:**
   ```bash
   python main.py
   ```
   *(Nota: El sistema generará automáticamente los archivos `historial_gastos.db` e `historial_gastos.txt` en el primer inicio).*

---

### 📄 Licencia

Este proyecto está bajo la Licencia MIT. Libre para fines educativos y desarrollo profesional continuo.
