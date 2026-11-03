
from graphviz import Digraph
from pathlib import Path

# Crear carpeta de documentación
Path("docs").mkdir(exist_ok=True)

# Crear diagrama C4
dot = Digraph(
    "C4_Contexto",
    filename="docs/c4_contexto",
    format="png"
)

# Configuración general
dot.attr(
    rankdir="TB",
    bgcolor="white",
    dpi="300",
    pad="0.35",
    nodesep="0.7",
    ranksep="0.9"
)

dot.attr(
    "node",
    shape="box",
    style="rounded,filled",
    fontname="Arial",
    fontsize="14",
    margin="0.30,0.22"
)

# Actor principal
dot.node(
    "usuario",
    "Estudiante / Investigador\n"
    "[Persona]\n"
    "Ejecuta y evalúa el modelo",
    fillcolor="#E5EEFC",
    color="#3269B2",
    fontcolor="#173B77"
)

# Sistema principal
dot.node(
    "sistema",
    "Sistema de clasificación de tumores\n"
    "[Sistema de software]\n"
    "Python + Scikit-learn\n"
    "Entrena, clasifica y evalúa registros",
    fillcolor="#165B9B",
    color="#104B82",
    fontcolor="white"
)

# Fuente externa
dot.node(
    "dataset",
    "Breast Cancer Wisconsin\n"
    "[Fuente externa de datos]\n"
    "Distribuido mediante Scikit-learn\n"
    "569 registros - 30 características",
    fillcolor="#687282",
    color="#687282",
    fontcolor="white"
)

# Relaciones
dot.edge(
    "usuario",
    "sistema",
    label="Ejecuta scripts y consulta resultados",
    fontsize="11"
)

dot.edge(
    "sistema",
    "dataset",
    label="Carga datos para entrenamiento y evaluación",
    fontsize="11"
)

# Generar imagen
ruta = dot.render(cleanup=True)

print("Diagrama C4 generado correctamente")
print("Ubicación:", ruta)
