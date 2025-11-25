# Waste Analysis Project

In this repository, I carry out an analysis and investigation regarding the impact that optimizing leaks and waste could have within restaurants and gastronomic businesses, focusing on prices from **Argentine wholesalers**.

---

## Project Context

This analysis originated from a real business need: assessing the economic viability of implementing a custom system designed to reduce waste and leaks in restaurants.  
The initial intent was to validate whether such a tool could generate a significant enough benefit to be commercially offered to a client in the gastronomy sector.

Therefore, the project does not rely on random or convenient simulated data. Instead, it answers a concrete business question:

**Is it worth investing in a waste-control system in the current Argentine economic context?**

---

## Objective

Analyze restaurant performance, probable losses, costs, and support the decision of implementing a system that enhances control over the raw materials used.

It includes:

- Identification of losses  
- Economic impact  
- Savings projection after optimization  
- Business KPIs and metrics  
- Final decision and recommendation  
- Final dashboard  

---

## Project Structure

```
analisis-gastronomico/
|-- data/ # raw, clean, and staging datasets
|-- scripts/ # reusable scripts and isolated processes
|-- notebooks/ # EDA, wrangling, conversion, and analysis notebooks
|-- equivalencias/ # dictionaries and mappings for category unification
|-- reporte-analitico.png # dashboard and final report
|-- requirements.txt # project dependencies
|-- README.md # this file
```

---

## Technologies Used

- **Python** (Jupyter Notebooks)  
- **Pandas** — cleaning, feature engineering, and transformation  
- **Matplotlib** — baseline visualizations  
- **Power BI** — analysis dashboard  

---

## General Process

### 1. Initial Exploration and Dataset Search

The project uses a combination of **simulated datasets** and **real prices** obtained from wholesalers and INDEC reports.

#### `Restaurant_Data.xlsx`

Base dataset containing sales and recipes for the fictional restaurant.

### Other sources consulted

- **INDEC** price reports  
- Gastronomy sector reports  
- Complementary sources for international prices  
- Currency rate APIs  

More information available in `data/README.md`.

---

### 2. Data Wrangling

Tasks performed:

- Removal of null values  
- Standardization to `snake_case`  
- Unit unification (g → kg)  
- Currency conversion when needed  
- General cleanup to maintain dataset consistency across notebooks  

> Column translation was kept isolated for optimization and performance reasons. Details in `scripts/README.md`.

---

### 3. Category Mapping to the Argentine Market

The restaurant dataset uses its own category scheme, while INDEC uses a completely different one.  
To enable joint analysis, the following were created:

- Mapping dictionaries  
- Subcategory equivalences  
- Unified classification criteria  

More details available in `equivalencias/README.md`.

---

### 4. Final Analysis

This section includes KPI creation, the Power BI dashboard, conclusions, and full graphic analysis.

---

## Usage Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Open the notebooks
Execution order inside `/notebooks`
```
eda.ipynb -> data_wrangling.ipynb -> paso_mercado.ipynb -> analisis_final.ipynb
```
> Important: After running the first notebook (EDA), if you prefer not to use the previously generated    `items_traducido.csv` file and want to regenerate it using traducir_df.py, be aware of potential translation errors due to limitations of automatic translation.

## Main results
- Maximum estimated savings percentage: 0.97% of monthly profit
- Annual monetary savings: $53.08M out of $4.37B (ARS)

> Results may vary depending on the original dataset, translation differences, or currency rates.

## Final Conclusion

The comprehensive analysis of waste, wholesale prices, and cost structure demonstrates that optimizing stock leaks in Argentine restaurants has a marginal economic impact.\
Even under a conservative scenario with full waste control, the potential improvement in profitability is below 1% of monthly profit.

This increase is insufficient to justify implementing an additional management system, considering:
- Software licensing and maintenance costs
- Staff training 
- Operational time needed to record stock movements
- Increased administrative complexity

Additionally, the analysis shows that the relative weight of food costs in Argentina is low compared to the overall business cost structure.\
Expenses such as rent, salaries, utilities, and social charges represent a significantly larger portion of operating costs and therefore offer much greater optimization potential.

## Executive Summary

Investing in a system focused solely on reducing raw-material losses is not economically viable for the Argentine gastronomy sector under current conditions.
Improvement efforts should instead focus on areas with greater financial impact, such as operational efficiency, renegotiation of fixed costs, and optimization of staff and space usage.




