# Análisis de Desperdicios y Ventas de un Restaurante
Este proyecto analiza el impacto económico de las fugas de stock en un restaurante. 
A partir de datos simulados con precios reales de mayoristas argentinos, estima pérdidas por categoría y predice ahorros posibles con la implementación de un sistema de gestión.

## Objetivo del proyecto
- Identificar las pérdidas (desde anuales hasta diarias) dadas a las fugas no identificadas
- Qué platos se están viendo mayormente afectados, para dar soluciones más específicas
- Demostrar los resultados luego de las optimizaciones
- Explicar la importancia de la implementación de estos sistemas y el abandono de las viejas y malas costumbres

## Estructura
```
analisis-de-desperdicios/
│-- data/                # datasets limpios y crudos
│-- notebook.ipynb       # análisis principal
│-- dashboard.png        # captura del dashboard
│-- requirements.txt     # librerías usadas
│-- README.md            # este archivo
```

## Tecnologías utilizadas
- Python, utilizando Jupyter Notebooks
- Pandas, para la limpieza y procesado de datasets
- Matplotlib, para el graficado y análisis de datos
- Power BI, para el diseño del dashboard

## Proceso de análisis
### **Exploración inicial y Búsqueda de datasets**
Para este proyecto se utilizó una combinación de **datasets simulados** y **fuentes reales** con el objetivo de representar el funcionamiento de un restaurante promedio.
 
#### **1. `Restaurant_Data.xlsx`**  
Dataset principal con el histórico de ventas y costos del restaurante ficticio.

**Hoja: Orders**
- `Date`: día de la transacción  
- `Time`: Horario de la transacción
- `Order Number`: Número de orden  
- `Item`: PK del item  
- `Count`: Cantidad vendida

**Hoja: Items**
- `Item`: PK del item   
- `Category`: Categoría del item (Desserts, Sides, Main Courses...)
- `Sub Category`: Sub-categoría del item (Pasta, Vegan...)
- `Item Name`: Nombre del item (Coffe, Beer, Burguers...) 
- `Price`: Costo del item (en dólares)
- `Cost`: Costo de producción

### Otras fuentes consultadas
Además del dataset principal, se analizaron:
- **Informe de precios del INDEC (`informe_indec.pdf`)**  
- **Artículos y reportes sectoriales** relacionados a desperdicio en gastronomía  
- **Publicaciones de mayoristas** para estimar costos reales  

> Más detalles sobre cada dataset, supuestos y estructura en:  
> `data/README.md`

--- 

### Limpieza de datos