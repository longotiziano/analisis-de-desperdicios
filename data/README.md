# Data
This directory contains the datasets used in the project, along with documentation and sources that justify the assumptions made.

---

## Directories

- **raw/**: Contains the raw, unprocessed data.  
- **staging/**: Stores intermediate CSV files generated after the EDA stage.  
- **clean/**: Contains fully processed data, ready for analysis.

---

## Datasets Used

### **1. Consumer Price Index (CPI - INDEC)**
Used for:
- obtaining reference prices for food items in Argentina  
- estimating inflation trends relevant to cost analysis  

Source:  
https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-5-31

---

### **2. Restaurant Cost and Sales Dataset (Kaggle)**  
Base dataset used to simulate the sales and cost structure of an average restaurant.  
An `.xlsx` file containing two sheets (`Orders` and `Items`) with original prices expressed in **USD**, later converted using updated exchange rates.

**Sheet: Orders**
- `Date`: Transaction date  
- `Time`: Transaction time  
- `Order Number`: Unique order ID  
- `Item`: Item primary key  
- `Count`: Units sold  

**Sheet: Items**
- `Item`: Item primary key  
- `Category`: Culinary category (Desserts, Sides, Main Courses...)  
- `Sub Category`: Subcategory (Pasta, Vegan...)  
- `Item Name`: Item name (Coffee, Beer, Burgers...)  
- `Price`: Item selling price (in USD)  
- `Cost`: Production cost  

Source:  
https://www.kaggle.com/datasets/virtualschool/restaurant-cost-and-sales-dataset

---

### **3. DolarAPI**
Used for:
- converting USD prices into ARS  
- simulating realistic scenarios based on up-to-date exchange rates  

API:  
https://dolarapi.com/v1/dolares/blue

---

## Complementary Research

- Statements from the CEO of PedidosYa on stock management in dark stores (Forbes)  
- Study on food waste in hotels and restaurants of Santa Fe (UNLP Repository)  
- UNEP Food Waste Index Report (2021)  
- Sector reports on average restaurant waste (FUDO)  

---

## Methodological Conclusions
The reviewed literature shows waste levels ranging from **4% to 17%**, depending on the country and the type of gastronomic operation.

For this project, a reference value of:

# **10% average food waste**

This number is used to estimate economic losses in the fictional restaurant and serves as a key parameter in the analytical model.
