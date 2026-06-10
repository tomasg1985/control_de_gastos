# 📊 Sistema de Gestión de Gastos Personales

Una solución interactiva y estructurada desarrollada en **Python** para la administración de finanzas personales. A través de una interfaz por línea de comandos organizada, el sistema permite registrar, monitorear y analizar flujos financieros diarios de forma ágil y centralizada para optimizar la toma de decisiones.

---

### 🚀 Características Técnicas

*   **Gestión Integral (CRUD):** Arquitectura con funciones dinámicas completas para la creación, lectura, actualización y eliminación de registros de gastos.
*   **Trazabilidad Automatizada:** Integración nativa del módulo `datetime` para realizar un sellado de tiempo (*timestamping*) automático con la fecha y hora exacta de cada transacción.
*   **Reportes Estadísticos en Tiempo Real:** Motor de análisis de datos que genera métricas clave instantáneas, incluyendo el total acumulado, promedio ponderado de egresos, y picos de consumo (valores máximos y mínimos).
*   **Experiencia de Usuario (UX):** Menús interactivos y alertas jerárquicas estilizadas con la librería **Colorama** para un feedback visual efectivo en consola.

---

### 🛠️ Stack Tecnológico y Requisitos

*   **Lenguaje:** Python 3.10+ *(Requerido para el soporte nativo de la estructura estructural `match-case`)*
*   **Librerías:** [Colorama](https://pypi.org) (Manejo y formateo de colores en la terminal)

---

### 📂 Estructura y Arquitectura de Archivos

El sistema implementa una separación clara entre la interfaz con el usuario y las reglas de negocio financieras:

1.  **`main.py`**: El punto de entrada de la aplicación. Orquesta el bucle de ejecución principal y la navegación del menú dinámico.
2.  **`logica_gastos.py`**: El núcleo analítico. Módulo autónomo que centraliza todas las funciones de procesamiento numérico, validación, cálculos estadísticos y manipulación de estructuras de datos.

---

### ⚙️ Instalación y Ejecución

Sigue estos pasos para clonar, configurar y ejecutar el sistema de forma local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd control_de_gastos
   ```

2. **Instalar las dependencias necesarias:**
   ```bash
   pip install colorama
   ```

3. **Iniciar la aplicación:**
   ```bash
   python main.py
   ```

---

### 📖 Guía Rápida de Operación

1.  Al iniciar el sistema, interactúa mediante el panel de opciones numéricas (1-8).
2.  **Registro de Transacciones:** Al agregar un gasto, ingresa la categoría, el monto numérico y una descripción. La aplicación inyectará el metadato temporal de manera automática.
3.  **Auditoría Financiera:** Utiliza la opción de *Generar Reporte* para desplegar el cuadro consolidado de estadísticas en tiempo real.

---

### 📄 Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo original para más información.
