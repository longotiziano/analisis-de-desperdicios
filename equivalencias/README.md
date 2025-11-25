# Equivalences Documentation
### _Strategy for Unifying Categories Between the Restaurant Dataset and INDEC_

This document explains the process used to map the restaurant’s categories to the raw materials listed in the INDEC report, in order to estimate real market costs in Argentina and perform a consistent economic analysis.

---

### Problem to Solve
Both sources use completely different classification structures, which made it impossible to calculate real costs without a correspondence system between the two schemas.

**For example:**  
While the restaurant dataset uses culinary categories, the INDEC report lists individual raw materials.

---

### Objective of the Equivalences System
- Enable real production cost estimation using INDEC prices.  
- Connect dishes to raw materials even when exact matches do not exist.  
- Maintain consistency, scalability, and flexibility within the analysis pipeline.

---

### Methodology and Assumptions
- A standard recipe structure was assumed such that the sum of its assigned values equals 5.  
- Subcategories of dishes were reviewed (main categories were irrelevant because they refer to the menu, not the dish itself).  
- The assigned weights do not represent exact quantities.  
- Consistency was prioritized above granularity.

**Example:**
```python
{
    'hamburgers': {
        'meats': 3,
        'bakery': 2,   # Each dictionary sums to 5 points
        'vegetables': 1
    },
    'salads': {
        'vegetables': 4,
        'oils': 1
    }
    # etc...
}
```
---

### Benefits of This Approach

- Reduces the likelihood of errors due to missing exact matches.
- Allows the use of real prices without replicating every individual recipe.
- Maintains consistency across very different datasets.
- Makes the project more scalable and realistic.

---

### Known Limitations

- Some product-level granularity is lost.
- Recipes can vary significantly between restaurants.
- Estimated costs represent a market average rather than exact formulations.

Even so, this method is suitable for general economic analysis, temporal comparisons, and estimating the financial impact of waste in a typical restaurant.

---

### Files

The files contained in this directory serve specific roles:
- `categorias_indec.py`: Contains the dictionary that assigns categories to the INDEC dataset.
- `equivalencias_pesos.py`: Dictionary that maps subcategories from the Items dataset to numerical weights of INDEC categories.
