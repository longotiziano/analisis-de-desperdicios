# Scripts

### Responsibilities
This folder contains logic and functions that:
- Perform isolated tasks  
- Prevent notebooks from becoming cluttered  
- Are reusable across the entire project  

---

### Notes on Dataset Translation
The dataset translation was executed using the `deep_translator` library which, although one of the most stable options, tends to be very slow.\
This was a problem because it significantly slowed down the notebook due to translating ~1500 cells.

To avoid this performance issue, I decided to handle the translation externally using the `traducir_df.py` script, which performs the translation separately and stores the result in a CSV.\
This approach dramatically improves execution speed across all notebooks.
