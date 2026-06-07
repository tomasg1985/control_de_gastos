# 📊 Sistema de Gestión de Gastos - TalentoLab

### 📝 Descripción
Este programa interactivo en Python ofrece una solución eficiente para la gestión de finanzas personales [1, 2]. A través de una interfaz de consola organizada, permite a los usuarios registrar, monitorear y analizar sus gastos diarios para una mejor toma de decisiones financieras [3, 4].

### 🚀 Características
*   **Gestión Integral (CRUD)**: Funciones completas para agregar, buscar, editar y eliminar registros de gastos de forma dinámica [3].
*   **Registro Automatizado**: Integración del módulo `datetime` para asignar automáticamente la fecha y hora exacta a cada registro [5, 6].
*   **Reportes Estadísticos**: Análisis de datos en tiempo real que muestra el total acumulado, promedio de gastos, y valores máximos/mínimos [7, 8].
*   **Interfaz Visual**: Menús interactivos y alertas resaltadas con colores mediante la librería `Colorama` [4, 9].

### 🛠️ Requisitos
*   **Python 3.10+** (requerido para la estructura `match-case`) [10].
*   **Colorama**: Instalación mediante `pip install colorama` [11].

### 📂 Estructura del Proyecto
*   `main.py`: Punto de entrada del programa. Contiene el bucle principal y la lógica del menú interactivo [12].
*   `logica_gastos.py`: Módulo que aloja todas las funciones de procesamiento, cálculos y manipulación de datos [13, 14].

### 📖 Instrucciones de Uso
1. Ejecutá `main.py`.
2. Seleccioná una opción del menú (1-8).
3. Para **Agregar Gasto**, ingresá la categoría, el monto y una breve descripción; el sistema se encargará de la fecha automáticamente [9, 15].
4. Utilizá la opción de **Generar Reporte** para obtener un resumen estadístico instantáneo de tus finanzas [8].
