
from sklearn.datasets import load_breast_cancer
import pandas as pd

# Cargar el dataset oficial
cancer = load_breast_cancer()

# Crear un DataFrame
df = pd.DataFrame(
    cancer.data,
    columns=cancer.feature_names
)

# Agregar la variable objetivo
df["diagnostico"] = cancer.target

# Crear una columna descriptiva
df["tipo_tumor"] = df["diagnostico"].map({
    0: "Maligno",
    1: "Benigno"
})

# Exportar a CSV
df.to_csv(
    "Breast_Cancer_Wisconsin.csv",
    index=False,
    encoding="utf-8-sig"
)

# Exportar a Excel
df.to_excel(
    "Breast_Cancer_Wisconsin.xlsx",
    index=False
)

print("Dataset descargado correctamente")
print("Registros:", len(df))
print("Columnas:", len(df.columns))
print(df.head())
