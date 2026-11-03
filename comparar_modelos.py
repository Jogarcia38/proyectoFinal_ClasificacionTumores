
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Cargar datos
df = pd.read_csv("Breast_Cancer_Wisconsin.csv")

X = df.drop(columns=["diagnostico", "tipo_tumor"])
y = (df["diagnostico"] == 0).astype(int)

# Misma división utilizada anteriormente
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Modelo de referencia
referencia = DummyClassifier(
    strategy="most_frequent"
)

referencia.fit(X_train, y_train)

# Modelo de regresión logística
logistica = Pipeline([
    ("escalador", StandardScaler()),
    ("modelo", LogisticRegression(
        max_iter=1000,
        random_state=42
    ))
])

logistica.fit(X_train, y_train)

# Comparación
resultados = []

for nombre, modelo in [
    ("Referencia", referencia),
    ("Regresión logística", logistica)
]:
    predicciones = modelo.predict(X_test)

    resultados.append({
        "Modelo": nombre,
        "Accuracy": accuracy_score(
            y_test, predicciones
        ),
        "Precision": precision_score(
            y_test, predicciones,
            zero_division=0
        ),
        "Recall": recall_score(
            y_test, predicciones,
            zero_division=0
        ),
        "F1-Score": f1_score(
            y_test, predicciones,
            zero_division=0
        )
    })

tabla = pd.DataFrame(resultados)

print("\nCOMPARACIÓN DE MODELOS")
print(tabla.to_string(index=False))

tabla.to_csv(
    "comparacion_modelos.csv",
    index=False
)

print("\nArchivo guardado: comparacion_modelos.csv")
