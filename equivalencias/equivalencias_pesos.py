equivalencias_pesos = {
    'sopas': {
        'verduras': 3,
        'legumbres_y_conservas': 1,
        'grasas_y_aceites': 1
    },
    'ensaladas': {
        'verduras': 4,
        'grasas_y_aceites': 1
    },
    'platos_de_aperitivo': {
        'panificados': 2,
        'verduras': 1,
        'carnes': 1,
        'grasas_y_aceites': 1
    },
    'mariscos': {
        'carnes': 4,   # se considera “carne” pero podés renombrar a “pescados_y_mariscos” si preferís
        'verduras': 1
    },
    'platos_de_carne': {
        'carnes': 4,
        'verduras': 1
    },
    'aves_de_corral': {
        'carnes': 3,
        'verduras': 1,
        'grasas_y_aceites': 1
    },
    'pastas': {
        'pastas_y_cereales': 3,
        'grasas_y_aceites': 1,
        'verduras': 1
    },
    'vegano': {
        'verduras': 3,
        'legumbres_y_conservas': 1,
        'pastas_y_cereales': 1
    },
    'papas': {
        'verduras': 2,
        'grasas_y_aceites': 3   # fritas o al horno siempre llevan aceite
    },
    'verduras': {
        'verduras': 5
    },
    'arroz': {
        'pastas_y_cereales': 4,
        'grasas_y_aceites': 1
    },
    'pan': {
        'panificados': 5
    },
    'tortas': {
        'panificados': 3,
        'lácteos': 1,
        'huevos': 1
    },
    'helado': {
        'lácteos': 4,
        'azucar': 1 if 'condimentos_y_otros' else 1
    },
    'tartas': {
        'panificados': 2,
        'verduras': 2,
        'huevos': 1
    },
    'pudines': {
        'lácteos': 3,
        'huevos': 1,
        'condimentos_y_otros': 1
    },
    'frutas': {
        'frutas': 5
    },
    'bebidas_no_alcoholicas': {
        'bebidas_no_alcoholicas': 5
    },
    'bebidas_alcoholicas': {
        'bebidas_alcoholicas': 5
    }
}
