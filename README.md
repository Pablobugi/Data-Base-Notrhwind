# 📊 Análisis de Ventas — Northwind Database

Proyecto end-to-end de análisis de datos sobre la base de datos relacional **Northwind**, cubriendo extracción, exploración, análisis avanzado y visualización de negocio con tres herramientas: **SQL**, **Python** y **Power BI**.

---

## 🎯 Objetivo

Responder preguntas de negocio reales a partir de datos transaccionales de ventas: ¿qué productos generan más ingresos?, ¿cómo evolucionan las ventas mes a mes?, ¿qué clientes regresan a comprar y cuáles no?

El proyecto está pensado como pieza de portafolio para mi transición hacia el análisis de datos, partiendo de mi formación en física.

---

## 🗂️ Estructura del repositorio

```
├── notebooks/
│   └── automatizacion_con_python.ipynb      # EDA, cohortes y visualizaciones en Python
├── sql/
│   └── analisis_con_sql.sqbpro              # Consultas SQL (DB Browser for SQLite)
├── powerbi/
│   └── analisis_con_power_bi.pbix           # Dashboard interactivo
├── images/
│   ├── top_10_productos_por_ingresos.png
│   ├── tendencia_de_ingresos_mensuales.png
│   ├── analisis_de_cohortes.png
│   └── tasa_de_retencion_de_clientes.png
├── data/
│   └── Northwind.db                         # Base de datos (ver sección Datos)
├── requirements.txt
└── README.md
```

---

## 🗃️ Datos

Se utiliza la base de datos de ejemplo **Northwind** (SQLite), que simula las ventas de una empresa importadora/exportadora de alimentos: pedidos, clientes, empleados, productos, categorías y proveedores.

Para ejecutar el proyecto, coloca el archivo `Northwind.db` dentro de la carpeta `data/`. El notebook y las consultas SQL referencian esta ruta de forma relativa.

---

## 🐍 1. Extracción y análisis exploratorio (Python + SQL)

**Notebook:** [`notebooks/automatizacion_con_python.ipynb`](notebooks/automatizacion_con_python.ipynb)

- Conexión a SQLite con `sqlite3` y consulta maestra con `JOIN` sobre 6 tablas (Orders, Customers, Employees, OrderDetails, Products, Categories)
- Carga directa a DataFrame con `pandas.read_sql_query`
- Validación de datos: dimensiones, valores nulos, producto más caro/barato
- **Análisis de cohortes:** segmentación de clientes según el mes de su primera compra, y seguimiento de su comportamiento en los meses siguientes
- **Tasa de retención:** porcentaje de clientes de cada cohorte que sigue comprando mes a mes
- Visualizaciones con `seaborn` / `matplotlib`: barplots, lineplots y heatmaps anotados

### Resultados

| Top 10 productos por ingresos | Tendencia de ingresos mensuales |
|---|---|
| ![Top productos](images/top_10_productos_por_ingresos.png) | ![Tendencia mensual](images/tendencia_de_ingresos_mensuales.png) |

| Análisis de cohortes (ingresos) | Tasa de retención de clientes |
|---|---|
| ![Cohortes](images/analisis_de_cohortes.png) | ![Retención](images/tasa_de_retencion_de_clientes.png) |

**Insight destacado:** la cohorte de clientes de julio de 1996 no solo generó el mayor ingreso en su primer mes ($37,780), sino que fue la que mejor se sostuvo en el tiempo, con actividad de compra hasta 7 meses después — el tipo de patrón que en un contexto real llevaría a investigar qué canal o campaña originó esos clientes.

---

## 🗄️ 2. Consultas SQL

**Archivo:** [`sql/analisis_con_sql.sqbpro`](sql/analisis_con_sql.sqbpro) (DB Browser for SQLite)

Batería de consultas de negocio, entre ellas:

- Clientes por país
- Productos con precio por encima del promedio
- Top 3 empleados con más órdenes
- Clientes que nunca han comprado (`LEFT JOIN` + `IS NULL`)
- Top 10 productos más vendidos por ingresos
- Ventas mensuales (`strftime`)
- Categorías más rentables y ticket promedio
- Clientes con ingreso por encima del promedio usando **CTEs** (`WITH`)
- Ventas por país y categoría con tablas pivote manuales (`CASE WHEN` + `SUM`)

---

## 📊 3. Dashboard interactivo (Power BI)

**Archivo:** [`powerbi/analisis_con_power_bi.pbix`](powerbi/analisis_con_power_bi.pbix)

Dashboard de dos páginas construido sobre el mismo dataset:

- **Ingresos segmentados por país:** mapa interactivo, ingresos por producto y KPIs (ingresos totales, órdenes, ticket promedio) que se recalculan según el país seleccionado
- **Ingresos por fecha:** tendencia mensual de ingresos y distribución porcentual por categoría de producto, con filtros de país y año

> 🎥 Puedes ver una demo en video del dashboard en mi publicación de LinkedIn: *(agregar enlace)*

---

## 🛠️ Stack técnico

- **Python:** pandas, seaborn, matplotlib, sqlite3, Jupyter Notebook
- **SQL:** SQLite (JOINs, subconsultas, CTEs, agregaciones, `CASE WHEN`)
- **BI:** Power BI (modelado, DAX, slicers, mapas)

---

## ▶️ Cómo ejecutar el proyecto

1. Clona el repositorio
2. Coloca `Northwind.db` dentro de la carpeta `data/`
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Abre el notebook y ejecuta las celdas en orden:
   ```bash
   jupyter notebook notebooks/automatizacion_con_python.ipynb
   ```
5. El archivo `.sqbpro` se abre con [DB Browser for SQLite](https://sqlitebrowser.org/)
6. El archivo `.pbix` se abre con [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Windows)

---

## 📬 Contacto

Si tienes comentarios o sugerencias sobre el proyecto, no dudes en contactarme. Estoy en transición hacia roles de análisis de datos y siempre abierto a feedback.

*(Agregar aquí: LinkedIn / correo)*
