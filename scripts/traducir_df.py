from deep_translator import GoogleTranslator
from scripts.utils import aplicar_funcion_df
import pandas as pd
import time

# Traducir DataFrame "Items" y las columnas que quiero traducir
traductor = GoogleTranslator(source='en', target='es').translate

# Leer CSV
dir_staging = r'.\data\staging'
df_items = pd.read_csv(dir_staging + r'\items.csv')  

# Limpio nulos para que no haya errores a la hora de la traducción
df_items = df_items.dropna()

# Traducción de columnas específicas (aprox 216 traducciones)
t0 = time.perf_counter()
print("Comenzando traducción...")

aplicar_funcion_df(df_items, [["Category", "Sub Category", "Item Name"]], traductor)

t1 = time.perf_counter()
print(f"Traducción finalizada -> Tiempo: {t1 - t0:.2f} segundos")

# Guardado en CSV
df_items.to_csv(dir_staging + r'\items_traducido.csv', index=False)



