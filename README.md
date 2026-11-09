# ![Proyecto Final Clasificacion de Tumores](https://capsule-render.vercel.app/api?type=transparent&color=0:FFFFFF,100:FFFFFF&height=65&section=header&text=Proyecto%20final%20clasificación%20de%20tumores&fontSize=28&fontColor=3D45F2&fontAlignY=50&animation=none)

Proyecto de Machine Learning para la clasificación de tumores mediante modelos supervisados.

## Problema que resolverá el proyecto

Este proyecto busca desarrollar un modelo de Machine Learning capaz de clasificar tumores mamarios como benignos o malignos a partir de características obtenidas de muestras celulares. Para ello, se utiliza el conjunto de datos Breast Cancer Wisconsin, que contiene información sobre diferentes características de los tumores.

La finalidad es apoyar el análisis de datos mediante técnicas de inteligencia artificial, permitiendo que el modelo identifique patrones y realice predicciones sobre nuevos registros. De esta manera, se puede evaluar qué tan bien un algoritmo de clasificación es capaz de diferenciar entre ambos tipos de tumores.

## Selección y justificación del modelo

Para este proyecto se seleccionó la Regresión Logística como modelo de Machine Learning, este modelo permite clasificar la información en dos categorías, por lo que resulta adecuado para identificar si un tumor es benigno o maligno a partir de las características presentes en el dataset Breast Cancer Wisconsin.

Asimismo la Regresión Logística es un modelo sencillo, fácil de implementar y ampliamente utilizado en problemas de clasificación; además, permite obtener resultados de manera rápida y evaluar su desempeño mediante métricas como Accuracy, Precision, Recall y F1-Score.

## Descripción del dataset

### Conjunto de datos utilizado

Para el desarrollo de este proyecto se utilizó el conjunto de datos Breast Cancer Wisconsin (Diagnostic), disponible en la biblioteca Scikit-learn, este dataset contiene información sobre características de muestras celulares obtenidas de tumores mamarios y se utiliza comúnmente en proyectos de aprendizaje automático para clasificación. El conjunto de datos está compuesto por 569 registros, de los cuales 357 corresponden a tumores benignos y 212 a tumores malignos.

### Ejemplo de registros

![Evidencia 1](Imagenes/1.%20Tabla%20dataset.png)

### Variables del dataset y objetivo del modelo

El conjunto de datos Breast Cancer Wisconsin (Diagnostic) contiene 30 variables numéricas que describen diferentes características de las células analizadas en muestras de tejido mamario, algunas de las variables más importantes son el radio, la textura, el perímetro, el área, la suavidad, la compacidad, la concavidad y la simetría, estas características permiten describir la forma y estructura de las células presentes en cada muestra. En consecuencia, estas variables son utilizadas como variables predictoras, es decir, son los datos que el modelo analiza para realizar una predicción en donde la variable objetivo es el diagnóstico del tumor, que puede tener dos resultados: benigno o maligno.

Asimismo el objetivo del modelo es aprender a identificar patrones en los datos para determinar si un tumor corresponde a la categoría de benigno o maligno. De esta manera, cuando reciba un nuevo registro con características similares, podrá realizar una predicción basándose en lo aprendido durante el entrenamiento.

### Aplicación de métricas de evaluación

Para evaluar el desempeño del modelo de Regresión Logística, se utilizaron métricas de clasificación que permiten medir qué tan bien identifica los tumores benignos y malignos, estas métricas se calcularon utilizando el conjunto de datos de prueba y los resultados obtenidos por el modelo.

### Resultados obtenidos

![Evidencia 2](Imagenes/2.%20Tabla%20con%20los%20resultados%20.png)

### Interpretación de las métricas

- **Accuracy:** indica el porcentaje total de predicciones correctas realizadas por el modelo, en este caso, el modelo clasificó correctamente el 96,49 % de los registros evaluados.

- **Precision:** muestra qué tan acertadas fueron las predicciones de tumores malignos, el resultado obtenido fue del 97,50 %, lo que significa que la mayoría de los casos identificados como malignos realmente pertenecían a esa categoría.

- **Recall:** mide la capacidad del modelo para detectar los casos malignos reales, el valor de 92,86 % indica que logró identificar correctamente la mayoría de los tumores malignos presentes en los datos de prueba.

- **F1-Score:** combina la precisión y la sensibilidad en una sola medida, el resultado de 95,12 % muestra un equilibrio adecuado entre ambas métricas.

### Matriz de confusión

Para complementar la evaluación del modelo de Regresión Logística, se utilizó una matriz de confusión que permite comparar las predicciones realizadas por el modelo con los valores reales del conjunto de prueba. Esta herramienta facilita la identificación de los aciertos y errores de clasificación.

![Evidencia 3](Imagenes/3.%20Matriz%20de%20confusion.png)

### Interpretación de la matriz

- **71 verdaderos negativos (VN):** tumores benignos que fueron clasificados correctamente como benignos.

- **39 verdaderos positivos (VP):** tumores malignos que fueron clasificados correctamente como malignos.

- **1 falso positivo (FP):** tumor benigno que fue clasificado incorrectamente como maligno.

- **3 falsos negativos (FN):** tumores malignos que fueron clasificados incorrectamente como benignos.

### Significado de los resultados de la matriz de confusión

La matriz de confusión permite identificar los aciertos y errores que comete el modelo al clasificar los tumores como benignos o malignos, en este proyecto se considera que un tumor maligno es el caso positivo.

imagen

En general, el modelo acertó en la mayoría de los casos, identificando correctamente 39 tumores malignos y 71 tumores benignos; sin embargo, cometió algunos errores: clasificó un tumor benigno como maligno y tres tumores malignos como benignos, estos últimos son los más importantes de analizar, ya que representan casos que el modelo no logró detectar correctamente. En total, el modelo realizó 110 clasificaciones correctas y 4 incorrectas sobre 114 registros evaluados, lo que demuestra un buen desempeño para los objetivos académicos del proyecto.

## Análisis ético del modelo

El uso de técnicas de Machine Learning en el análisis de información relacionada con la salud requiere considerar aspectos éticos que van más allá de la precisión de los resultados, aunque el modelo de Regresión Logística obtuvo un buen desempeño durante las pruebas, es importante reconocer sus limitaciones y los riesgos asociados a su utilización.

### Posibles sesgos en los datos

El conjunto de datos utilizado contiene una mayor cantidad de registros benignos que malignos, esta diferencia podría influir en el aprendizaje del modelo y afectar sus predicciones en algunos casos; sin embargo, con la información disponible no es posible confirmar la existencia de un sesgo discriminatorio ni evaluar el comportamiento del modelo en diferentes grupos de población.

### Privacidad de la información

El dataset empleado no contiene nombres, documentos de identidad ni otros datos personales de pacientes, aun así, cuando se trabaja con información relacionada con la salud es importante garantizar un manejo responsable de los datos, evitando accesos no autorizados y respetando los principios de confidencialidad.

### Impacto social

Los resultados obtenidos muestran que el modelo puede clasificar correctamente la mayoría de los registros analizados; no obstante, también se identificaron errores de clasificación, incluyendo casos malignos que fueron identificados como benignos. Si un sistema de este tipo se utilizara sin supervisión adecuada, podría afectar la toma de decisiones y generar consecuencias negativas para las personas involucradas.

### Transparencia y responsabilidad

Es importante que los usuarios conozcan qué datos utiliza el modelo, cómo se generan las predicciones y cuáles son sus limitaciones, la transparencia permite interpretar los resultados de manera adecuada y evita confiar plenamente en decisiones automatizadas sin una revisión humana.

### Uso responsable
Este proyecto fue desarrollado con fines académicos y de aprendizaje, por lo tanto, sus resultados deben utilizarse únicamente para demostrar la aplicación de técnicas de Machine Learning y no como una herramienta para realizar diagnósticos médicos o sustituir la opinión de profesionales de la salud.

## Análisis de posibles sesgos del modelo o del dataset

El conjunto de datos utilizado tiene más casos de tumores benignos que malignos, ya que cuenta con 357 registros benignos y 212 malignos, esto puede hacer que el modelo aprenda mejor las características de los casos más frecuentes y tenga más dificultad para identificar algunos casos malignos.

Asimismo, la información disponible no permite saber si los datos representan adecuadamente a todas las personas o poblaciones, por esta razón, no se puede asegurar que el modelo obtenga los mismos resultados en otros grupos o situaciones. Aunque el desempeño general fue bueno, es importante seguir evaluándolo con más datos para comprobar su confiabilidad.

## Equidad, privacidad, impacto social y uso responsable de los datos

- **Equidad:** El modelo fue entrenado con datos de tumores benignos y malignos para aprender a clasificarlos correctamente. Sin embargo, no se dispone de información suficiente para verificar si el modelo funciona de la misma manera en diferentes grupos de personas, por lo que sus resultados deben interpretarse con precaución.

- **Privacidad:** El conjunto de datos utilizado no contiene nombres, documentos de identidad ni información personal de los pacientes. Aun así, es importante garantizar un manejo responsable de los datos y utilizar la información únicamente para fines académicos.

- **Impacto social:** Este tipo de modelos puede apoyar el análisis de información y facilitar el aprendizaje sobre Machine Learning. Sin embargo, una clasificación incorrecta podría generar conclusiones equivocadas si se utiliza sin supervisión adecuada.

- **Uso responsable de los datos:** El proyecto fue desarrollado con fines educativos y no debe utilizarse para realizar diagnósticos médicos reales. Los resultados obtenidos deben considerarse como una herramienta de apoyo al aprendizaje y no como una decisión definitiva sobre la salud de una persona.

## Reflexionar sobre la justicia y transparencia en la toma de decisiones.

La justicia en un modelo de Machine Learning implica que las decisiones se basen en los datos analizados y no favorezcan o perjudiquen de manera injustificada a un grupo determinado, en este proyecto no fue posible verificar el comportamiento del modelo en diferentes poblaciones, por lo que los resultados deben interpretarse con precaución y considerando las limitaciones de los datos utilizados.

La transparencia es fundamental para comprender cómo se obtienen las predicciones y cuáles son las limitaciones del modelo; aunque la Regresión Logística obtuvo buenos resultados en las pruebas realizadas, también presentó algunos errores de clasificación, lo que demuestra que sus predicciones no son perfectas. Por esta razón, las decisiones basadas en el modelo deben contar con supervisión humana y utilizarse únicamente con fines académicos, evitando que sustituyan el criterio de profesionales especializados.

## Conclusiones técnicas

El modelo de Regresión Logística presentó un buen desempeño en la clasificación de tumores benignos y malignos utilizando el conjunto de datos Breast Cancer Wisconsin, durante la evaluación alcanzó una exactitud (Accuracy) del 96,49 %, lo que demuestra que logró clasificar correctamente la mayoría de los registros analizados. Además, obtuvo valores altos de precisión, sensibilidad y F1-Score, lo que indica un desempeño equilibrado en la identificación de ambas categorías.

La matriz de confusión mostró que el modelo realizó 110 clasificaciones correctas de 114 registros evaluados, aunque se presentaron algunos errores, especialmente tres casos malignos clasificados como benignos. A pesar de esta limitación, los resultados fueron superiores a los obtenidos por el modelo de referencia, por lo que se concluye que la Regresión Logística fue una alternativa adecuada para cumplir los objetivos académicos del proyecto y demostrar la aplicación de técnicas básicas de Machine Learning.

## Recomendaciones para mejorar

Aunque el modelo obtuvo buenos resultados durante las pruebas, existen algunas acciones que podrían mejorar su desempeño y confiabilidad; una de ellas es evaluar el modelo con nuevos conjuntos de datos para comprobar si mantiene resultados similares en situaciones diferentes. Esto permitiría validar mejor su capacidad de clasificación y reducir el riesgo de obtener resultados adecuados únicamente para los datos utilizados en el proyecto.

También se recomienda comparar la Regresión Logística con otros algoritmos de Machine Learning, como Árbol de Decisión o KNN, para determinar cuál ofrece mejores resultados. Además, sería conveniente buscar estrategias que permitan reducir los errores de clasificación, especialmente los casos malignos identificados como benignos, y continuar fortaleciendo el análisis ético y la validación de los resultados antes de considerar aplicaciones fuera del ámbito académico.











