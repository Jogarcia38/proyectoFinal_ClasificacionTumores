
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("Breast_Cancer_Wisconsin.csv")

# 1. Dimensiones
print("\n1. DIMENSIONES DEL DATASET")
print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])

# 2. Primeros registros
print("\n2. PRIMEROS 5 REGISTROS")
print(df.head())

# 3. Tipos de datos
print("\n3. TIPOS DE DATOS")
print(df.dtypes)

# 4. Valores nulos
print("\n4. VALORES NULOS")
print(df.isnull().sum())

# 5. Registros duplicados
print("\n5. REGISTROS DUPLICADOS")
print(df.duplicated().sum())

# 6. Distribución de diagnósticos
print("\n6. DISTRIBUCIÓN DE DIAGNÓSTICOS")
print(df["tipo_tumor"].value_counts())

# 7. Estadísticas descriptivas
print("\n7. ESTADÍSTICAS DESCRIPTIVAS")
print(df.describe())

# 8. Crear gráfico de distribución
conteo = df["tipo_tumor"].value_counts()

plt.figure(figsize=(8, 5))
barras = plt.bar(
    conteo.index,
    conteo.values,
    color=["steelblue", "coral"]
)

plt.title("Distribución de tumores por diagnóstico")
plt.xlabel("Tipo de tumor")
plt.ylabel("Número de registros")

for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        str(int(altura)),
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("distribucion_tumores.png", dpi=300)
plt.show()

