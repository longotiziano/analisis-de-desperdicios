# Análisis de Desperdicios y Ventas de un Restaurante
Este proyecto analiza el impacto económico de las fugas de stock en un restaurante. 
A partir de datos simulados con precios reales de **mayoristas argentinos**, estima pérdidas por categoría y predice ahorros posibles con la implementación de un sistema de gestión.

## Objetivo del proyecto
- Identificar las pérdidas (desde anuales hasta diarias) dadas a las fugas no identificadas
- Qué platos se están viendo mayormente afectados, para dar soluciones más específicas
- Demostrar los resultados luego de las optimizaciones
- Explicar la importancia de la implementación de estos sistemas y el abandono de las viejas y malas costumbres

## Estructura
```
analisis-de-desperdicios/
|-- data/                # datasets limpios y crudos
|-- notebooks/           # análisis principal
|-- scripts/             # lógica reutilizable y tareas
|-- equivalencias/       # diccionarios utilizados en equivalencias
|-- dashboard.png        # captura del dashboard
|-- requirements.txt     # librerías usadas
|-- README.md            # este archivo
```

## Tecnologías utilizadas
- Python, utilizando Jupyter Notebooks
- Pandas, para la limpieza y procesado de datasets
- Matplotlib, para el graficado y análisis de datos
- Power BI, para el diseño del dashboard

## Proceso de análisis
### 1. Exploración inicial y Búsqueda de datasets
Para este proyecto se utilizó una combinación de **datasets simulados** y **fuentes reales** con el objetivo de representar el funcionamiento de un restaurante promedio.
 
#### `Restaurant_Data.xlsx`
Dataset principal con el histórico de ventas y costos del restaurante ficticio.

> **Nota:**: La columna Cost (costo de producción en USD) no se utilizó en este análisis, ya que el enfoque se centra en costos del mercado argentino obtenidos de fuentes locales.

### Otras fuentes consultadas
Además del dataset principal, se analizaron:
- **Informe de precios del INDEC (`informe_indec.pdf`)**  
- **Artículos y reportes sectoriales** relacionados a desperdicio en gastronomía  

> Más detalles sobre cada dataset, supuestos y estructura en `data/README.md`

--- 

### 2. Data Wrangling
Luego de haber identificado en el **Exploratory Data Analysis** (EDA) las tareas encomendadas, se realizaron diversas tareas:
- Eliminación de valores nulos
- Traducción de DataFrames
- Formateo a `snake_case`
- Pasado a unidades en común (ej: precio en g -> precio en kg)
- Conversión de tipo de cambio

> **Nota**: La traducción del dataset fue aislada debido a tópicos de optimización, para más información acudir a `scripts/README.md` 

---

### 3. Feature Engineering
En esta etapa se generan nuevas variables, métricas y KPIs que aportan valor al análisis del negocio.
- Paso a mercado argentino
- Agregado de métricas y cálculos que dejan listos los datos para ser graficados
- KPIs
- Insights

**KPIs:**
- **Desperdicio general** -> % y $
- **Ganancia de categorías afectada** -> % (ej: pérdida de ganancia de un 7% en [categoría])
- Comparación temporal de ventas **con y sin optimización**

#### Paso a mercado argentino

En el paso a mercado argentino me enfrenté a un problema: el dataset del restaurante y el del INDEC **utilizan esquemas distintos**, lo que hacia imposible su comparación directa.\
Para resolverlo, se crearon diccionarios de equivalencias (con IA), donde cada categoría/subcategoría del restaurante fue mapeada a una categoría homogénea equivalente del INDEC. 

> En caso de querer revisión, los diccionarios se encuentran en el directorio `equivalencias/`

> Para más información acerca de la estrategia implementada y detalles técnicos asistir a `feature-engineering.ipynb`

---

### 4. Reporte en Power BI
Finalmente, desarrollé un reporte en Power BI, donde analizo, explico y muestro las diversas métricas y KPIs que me parecieron de valor para este
escenario hipotético.

**Insights clave encontrados:**
- Productos con más pérdidas 

---

### Diagrama de flujo de datos:
```
Raw Data -> EDA -> Wrangling -> Feature Engineering -> KPIs -> Dashboard
```