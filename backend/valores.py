import pandas as pd

item1 = [
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO"
]

item2 = [
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO"
]

valor1 = [
    37.5,
    25,
    19,
    9.5,
    4.75,
    2,
    0.85,
    0.425,
    0.250,
    0.10,
    0.75,
    0
]

valor2 = [
    37.5,
    25,
    1,
    9.5,
    4.75,
    2,
    0.85,
    0.425,
    0.250,
    0.150,
    0.075,
    0
]

item_1 = pd.DataFrame({
    "ITEM_1": item1
})

item_2 = pd.DataFrame({
    "ITEM_2": item2
})

valor_1 = pd.DataFrame({
    "PRECIO_UNITARIO_1": valor1
})

valor_2 = pd.DataFrame({
    "PRECIO_UNITARIO_2": valor2
})

# Crear la tercera columna con el valor mayor entre valor1 y valor2
#max_values = pd.DataFrame({
   # "VALOR_MAYOR": [max(v1, v2) for v1, v2 in zip(valor1, valor2)]
#})

# Concatenar las nuevas columnas a los DataFrames existentes
#item_1 = pd.concat([item_1, max_values], axis=1)
#item_2 = pd.concat([item_2, max_values], axis=1)

#print(item_1)
#print("\n")
#print(item_2)