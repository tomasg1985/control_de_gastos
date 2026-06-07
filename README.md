# 📊 Sistema de Gestión de Gastos

### 📝 Descripción
Este programa interactivo en Python ofrece una solución eficiente para la gestión de finanzas personales. A través de una interfaz de consola organizada, permite a los usuarios registrar, monitorear y analizar sus gastos diarios para una mejor toma de decisiones financieras.

### 🚀 Características
*   **Gestión Integral (CRUD)**: Funciones completas para agregar, buscar, editar y eliminar registros de gastos de forma dinámica.
*   **Registro Automatizado**: Integración del módulo `datetime` para asignar automáticamente la fecha y hora exacta a cada registro.
*   **Reportes Estadísticos**: Análisis de datos en tiempo real que muestra el total acumulado, promedio de gastos, y valores máximos/mínimos.
*   **Interfaz Visual**: Menús interactivos y alertas resaltadas con colores mediante la librería `Colorama`.

### 🛠️ Requisitos
*   **Python 3.10+** (requerido para la estructura `match-case`).
*   **Colorama**: Instalación mediante `pip install colorama`.

### 📂 Estructura del Proyecto
*   `main.py`: Punto de entrada del programa. Contiene el bucle principal y la lógica del menú interactivo.
*   `logica_gastos.py`: Módulo que aloja todas las funciones de procesamiento, cálculos y manipulación de datos.

### 📖 Instrucciones de Uso
1. Ejecutá `main.py`.
2. Seleccioná una opción del menú (1-8).
3. Para **Agregar Gasto**, ingresá la categoría, el monto y una breve descripción; el sistema se encargará de la fecha automáticamente.
4. Utilizá la opción de **Generar Reporte** para obtener un resumen estadístico instantáneo de tus finanzas.
