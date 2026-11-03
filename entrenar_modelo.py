
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ============================================
# 1. CARGAR EL DATASET
# ============================================

df = pd.read_csv("Breast_Cancer_Wisconsin.csv")

print("\nINFORMACIÓN DEL DATASET")
print("--------------------------------")
print("Total de registros:", len(df))
print("Total de columnas:", len(df.columns))

# ============================================
# 2. SEPARAR VARIABLES
# ============================================

# Variables predictoras
X = df.drop(
    columns=["diagnostico", "tipo_tumor"]
)

# Variable objetivo:
# 1 = Maligno
# 0 = Benigno
# En el dataset original:
# 0 = Maligno y 1 = Benigno

y = (df["diagnostico"] == 0).astype(int)

# ============================================
# 3. DIVIDIR DATOS
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nDIVISIÓN DE DATOS")
print("--------------------------------")
print("Registros de entrenamiento:", len(X_train))
print("Registros de prueba:", len(X_test))

# ============================================
# 4. CREAR EL MODELO
# ============================================

modelo = Pipeline([
    ("escalador", StandardScaler()),
    ("clasificador", LogisticRegression(
        max_iter=1000,
        random_state=42
    ))
])

# ============================================
# 5. ENTRENAR EL MODELO
# ============================================

modelo.fit(X_train, y_train)

print("\nENTRENAMIENTO FINALIZADO")

# ============================================
# 6. REALIZAR PREDICCIONES
# ============================================

y_pred = modelo.predict(X_test)

# ============================================
# 7. CALCULAR MÉTRICAS
# ============================================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nRESULTADOS DEL MODELO")
print("--------------------------------")

print(f"Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"Precision: {precision:.4f} ({precision*100:.2f}%)")
print(f"Recall:    {recall:.4f} ({recall*100:.2f}%)")
print(f"F1-Score:  {f1:.4f} ({f1*100:.2f}%)")

# ============================================
# 8. REPORTE DE CLASIFICACIÓN
# ============================================

print("\nREPORTE DE CLASIFICACIÓN")
print("--------------------------------")

print(classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Benigno", "Maligno"],
    zero_division=0
))

# ============================================
# 9. MATRIZ DE CONFUSIÓN
# ============================================

matriz = confusion_matrix(
    y_test,
    y_pred,
    labels=[0, 1]
)

print("\nMATRIZ DE CONFUSIÓN")
print("--------------------------------")
print(matriz)

# ============================================
# 10. INTERPRETAR LA MATRIZ
# ============================================

vn, fp, fn, vp = matriz.ravel()

print("\nINTERPRETACIÓN DE RESULTADOS")
print("--------------------------------")

print("Verdaderos negativos (VN):", vn)
print("Falsos positivos (FP):", fp)
print("Falsos negativos (FN):", fn)
print("Verdaderos positivos (VP):", vp)

print("\nSIGNIFICADO:")
print("VN: Tumores benignos correctamente clasificados.")
print("FP: Tumores benignos clasificados como malignos.")
print("FN: Tumores malignos clasificados como benignos.")
print("VP: Tumores malignos correctamente clasificados.")

# ============================================
# 11. GRAFICAR MATRIZ DE CONFUSIÓN
# ============================================

visualizacion = ConfusionMatrixDisplay(
    confusion_matrix=matriz,
    display_labels=["Benigno", "Maligno"]
)

visualizacion.plot(
    cmap="Blues",
    values_format="d"
)

plt.title(
    "Matriz de confusión - Regresión Logística"
)

plt.xlabel("Diagnóstico predicho")
plt.ylabel("Diagnóstico real")

plt.tight_layout()

# ============================================
# 12. GUARDAR GRÁFICO
# ============================================

plt.savefig(
    "matriz_confusion.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nGráfico guardado: matriz_confusion.png")

# ============================================
# 13. MOSTRAR GRÁFICO
# ============================================

plt.show()

print("\nPROCESO FINALIZADO CORRECTAMENTE")
