# Scripts

### Responsabilidades
Esta carpeta se encarga de contener lógica y funciones que:
- Buscan cumplir tareas aisladas
- Eviten el manchado de las notebooks
- Sean reutilizables a través de todo el proyecto

---

### Aclaración sobre la traducción del dataset
La traducción del dataset fue ejecutada con la librería `deep_translator`, que si bien es la más estable, suelen demorar mucho sus procesos. Esto era grave, ya que relentizaba todo el notebook por una simple traducción de ~1500 celdas, por lo que decidí manejarla de manera externa con el script `traducir_df.py`, que traduce externamente y almacena en un CSV, aumentando así de manera drástica la velocidad del código. 