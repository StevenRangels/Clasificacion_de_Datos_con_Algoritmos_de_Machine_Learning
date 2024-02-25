import sqlite3,pandas as pd, csv, numpy as np

conexion = sqlite3.connect(r'D:\Python2\datos_sensores.db')

query = """
SELECT 
    db.id, 
    o.sensor_orion, 
    v.sensor_vega,
    p.sensor_polaris, 
    a.sensor_antares,
    CASE 
        WHEN c.etiqueta = 'Positivo' THEN 1
        WHEN c.etiqueta = 'Negativo' THEN 0
        ELSE 3	  
    END AS etiqueta_numerica
FROM datos_basicos db
JOIN orion o ON o.id = db.id
JOIN vega v ON v.id = db.id
JOIN polaris p ON p.id = db.id
JOIN antares a ON a.id = db.id
JOIN clasificacion c ON c.id = db.id
WHERE db.id BETWEEN 1 AND 300000;
"""

dataset = pd.read_sql_query(query,conexion)

# Creación y entrenamiento del modelo
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

X = dataset.drop(['id', 'etiqueta_numerica'], axis=1)  # Predictores
y = dataset['etiqueta_numerica']  # Variable objetivo

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0004, random_state=42)

# Crear el modelo de Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo
rf_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predicciones = rf_model.predict(X_test)

# Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, predicciones)
print(f"\nPrecisión del modelo: {accuracy:.2f}")

query_sin_clasificar = """
SELECT 
    db.id, 
    o.sensor_orion, 
    v.sensor_vega,
    p.sensor_polaris, 
    a.sensor_antares,
    CASE 
        WHEN c.etiqueta = 'Positivo' THEN 1
        WHEN c.etiqueta = 'Negativo' THEN 0
        ELSE 3	  
    END AS etiqueta_numerica
FROM datos_basicos db
JOIN orion o ON o.id = db.id
JOIN vega v ON v.id = db.id
JOIN polaris p ON p.id = db.id
JOIN antares a ON a.id = db.id
JOIN clasificacion c ON c.id = db.id
WHERE db.id BETWEEN 300001 AND 300100;
"""

# Leer datos sin clasificar
dataset_sin_clasificar = pd.read_sql_query(query_sin_clasificar, conexion)

# predicciones con datos sin clasificar usando el modelo entrenado
predicciones_sin_clasificar = rf_model.predict(dataset_sin_clasificar.drop(['id', 'etiqueta_numerica'], axis=1))

# Imprimir predicciones
print(predicciones_sin_clasificar)

vector_modificado = ['Positivo' if valor == 1 else 'Negativo' for valor in predicciones_sin_clasificar]

print(vector_modificado)

id_valores = list(range(300001, 300102))
data = list(zip(id_valores, vector_modificado))

file_name = 'predicciones.csv'

with open(file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['id', 'etiqueta'])
    csv_writer.writerows(data)

print(f'Se ha creado el archivo CSV: {file_name}')