# Clasificación de Datos con Algoritmos de Machine Learning

En este repositorio, clasificamos los datos faltantes de las muestras de mediciones de satélites almacenadas en una base de datos SQLite (.db).

## Objetivos

1. Desarrollar e implementar un modelo de machine learning con el objetivo de alcanzar un índice de respuesta cercano al 100% de fidelidad. La fidelidad se refiere a la capacidad del modelo para proporcionar respuestas precisas y coherentes.

2. Implementar un sistema de asignación de valores (positivos o negativos) basado en su tamaño y categoría, con el propósito de clasificar las mediciones faltantes de los sensores. Este objetivo tiene como finalidad fortalecer la integridad y completitud de los datos, posibilitando así un análisis más sólido y preciso. Este enfoque estratégico contribuirá a la mejora global de la calidad de los datos, permitiendo una interpretación más informada y eficiente de las lecturas de los sensores.

## Descripción

1. Conexión a la base de datos SQLite:
- Se establece una conexión con una base de datos SQLite llamada datos_sensores.db

2. Consulta SQL para datos clasificados:
- Se define una consulta SQL para extraer información de las tablas datos_basicos, orion, vega, polaris, antares y clasificacion para identificadores (id) en el rango de 1 a 300,000.
- La consulta selecciona el identificador (id), valores de sensores y asigna una etiqueta numérica basada en la columna clasificacion.etiqueta.

3. Lectura de datos en un DataFrame de Pandas:
- Utilizando Pandas, se ejecuta la consulta SQL y se carga el resultado en un DataFrame denominado dataset.

4. División de datos y entrenamiento del modelo:
- Los datos se dividen en predictores (X) y variable objetivo (y).
- Se dividen los datos en conjuntos de entrenamiento y prueba.
- Se crea y entrena un modelo de clasificación de Bosques Aleatorios (RandomForestClassifier).

5. Predicciones y evaluación del modelo:
- Se realizan predicciones en el conjunto de prueba y se evalúa la precisión del modelo utilizando métricas como la precisión.
- Se imprime la precisión del modelo en el conjunto de prueba.

6. Consulta SQL para datos no clasificados:
- Se define otra consulta SQL para obtener datos no clasificados para identificadores en el rango de 300,001 a 300,100.

7. Predicciones con datos no clasificados:
- Se ejecuta la consulta SQL y se realizan predicciones en los datos no clasificados utilizando el modelo previamente entrenado.

8. Modificación y escritura en un archivo CSV:
- Se modifica la salida numérica de las predicciones a etiquetas ('Positivo' o 'Negativo') y se crea un archivo CSV llamado 'predicciones.csv' con los resultados.

9. Impresión de resultados:
- Se imprime la salida de las predicciones no clasificadas y el nombre del archivo CSV creado.

## Resultados  

1. Índice de Fidelidad del Modelo:
- Después de la implementación y evaluación del modelo de machine learning, se logró un impresionante índice de fidelidad del 93%. Esto indica que el modelo tiene una capacidad muy alta para proporcionar respuestas precisas, casi alcanzando el nivel objetivo del 100%.

2. Clasificación Exitosa de Mediciones Faltantes:
- El modelo destacó por su buen rendimiento al clasificar las 100 mediciones faltantes de los sensores. Su capacidad para llevar a cabo esta clasificación permitió asignar con una alta precisión  cada medición a su respectivo valor, ya sea positivo o negativo.

## Conclusiones

1. Alto Índice de Fidelidad del Modelo:
- Tras la implementación y evaluación del modelo de machine learning, se logró un impresionante índice de fidelidad del 93%. Este resultado sugiere que el modelo tiene una capacidad excepcional para proporcionar respuestas precisas, aproximándose al objetivo del 100%.

2. Éxito en la Clasificación de Mediciones Faltantes:
- El modelo exhibió un rendimiento notable al clasificar las 100 mediciones faltantes de los sensores. Esta capacidad de clasificación permitió asignar cada medición a su correspondiente valor, ya sea positivo o negativo. Esta mejora sustancial en la calidad y utilidad de los datos contribuye significativamente a la confiabilidad de la información recopilada, fortaleciendo la base para análisis posteriores y decisiones informadas basadas en los resultados del modelo.

3. Mejora en la Integridad y Completitud de los Datos:
- La implementación de un sistema de asignación de valores basado en el tamaño y categoría fortaleció la integridad y totalidad de los datos. Esta estrategia contribuye a un análisis más sólido y preciso, mejorando globalmente la calidad de los datos. La interpretación más informada y eficiente de las lecturas de los sensores es posible gracias a este enfoque estratégico.

4. Generación Eficiente de Resultados en Formato CSV:
- El proceso de modificación y escritura de las predicciones en un archivo CSV ("predicciones.csv") facilita la compartición y análisis posterior de los resultados. Este archivo contiene la información clasificada de las mediciones no etiquetadas, mejorando la accesibilidad y utilidad de los resultados del modelo.