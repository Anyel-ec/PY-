## Título: **Análisis de Sentimientos en Reseñas de Películas Usando Naive Bayes**

### Descripción

Este proyecto utiliza un clasificador Naive Bayes para analizar el sentimiento en reseñas de películas del dataset IMDB. Se emplea la técnica de Bolsa de Palabras para la representación de texto y se evalúa el rendimiento del modelo usando métricas estándar de clasificación. La visualización de la matriz de confusión proporciona una comprensión clara del desempeño del modelo.

### Requisitos

- Python 3.x
- pandas
- scikit-learn
- seaborn
- matplotlib

Puedes instalar las dependencias necesarias usando pip:

```bash
pip install pandas scikit-learn seaborn matplotlib
```

### Archivo Principal

El archivo principal del proyecto realiza los siguientes pasos:

1. **Cargar el Dataset**: Lee un archivo CSV que contiene reseñas de películas y sus sentimientos (positivo/negativo).
2. **Preparar los Datos**: Mapea los sentimientos a valores binarios y divide el dataset en conjuntos de entrenamiento y prueba.
3. **Representación de Texto**: Convierte las reseñas de texto en una matriz de características utilizando la técnica de Bolsa de Palabras.
4. **Entrenar el Modelo**: Ajusta un clasificador Naive Bayes multinomial con los datos de entrenamiento.
5. **Evaluar el Modelo**: Predice los sentimientos de las reseñas de prueba y calcula métricas de rendimiento como la precisión, la matriz de confusión y el reporte de clasificación.
6. **Visualización**: Muestra una matriz de confusión en forma de gráfico para una interpretación visual de los resultados.

### Cómo Ejecutar el Proyecto

1. **Coloca el Dataset**: Asegúrate de que el archivo CSV del dataset (`IMDB Dataset.csv`) esté en la ruta correcta (`/content/drive/MyDrive/Datasets/IMDB Dataset.csv`), o actualiza la ruta en el código según sea necesario.

2. **Ejecuta el Código**: Corre el script en tu entorno Python para realizar el análisis de sentimientos.

```python
python nombre_del_script.py
```

### Resultados

El script imprimirá los siguientes resultados en la consola:

- **Precisión**: Mide la proporción de predicciones correctas.
- **Matriz de Confusión**: Una tabla que muestra las predicciones verdaderas frente a las predicciones falsas.
- **Reporte de Clasificación**: Incluye precisión, recall, y F1-score para cada clase.

Además, se generará una visualización de la matriz de confusión utilizando `seaborn` y `matplotlib`.

### Ejemplo de Salida

```
Accuracy: 0.8448

Confusion Matrix:
 [[4218  743]
 [ 809 4230]]

Classification Report:
               precision    recall  f1-score   support

           0       0.84      0.85      0.84      4961
           1       0.85      0.84      0.84      5039

    accuracy                           0.84     10000
   macro avg       0.84      0.84      0.84     10000
weighted avg       0.84      0.84      0.84     10000
```

### Visualización

La matriz de confusión se visualiza en un gráfico de calor, que facilita la interpretación de los resultados del modelo.

### Contribuciones

Las contribuciones y mejoras al proyecto son bienvenidas. Si deseas contribuir, por favor, abre un issue o envía un pull request.

### Licencia

Este proyecto está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT). Puedes utilizar, modificar y distribuir el código según los términos de esta licencia.

### Contacto

Para cualquier pregunta o comentario, puedes contactar al autor en Anyel EC