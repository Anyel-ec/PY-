# Identificación de Versos Alejandrinos en Poemas con LSTM

Este proyecto utiliza un modelo de Red Neuronal LSTM (Long Short-Term Memory) para identificar versos alejandrinos en poemas. Un verso alejandrino es un verso poético que consta de 14 sílabas. El modelo entrena en poemas tokenizados y predice si un verso dado es alejandrino o no.

## Descripción

El script realiza las siguientes tareas:

1. **Carga y preprocesamiento de datos:** Lee un archivo CSV con poemas, tokeniza el texto y convierte los poemas en secuencias de enteros.
2. **Contador de sílabas:** Implementa una función para contar el número de sílabas en un verso.
3. **Entrenamiento del modelo LSTM:** Construye, compila y entrena un modelo LSTM para clasificar versos como alejandrinos o no alejandrinos.
4. **Predicción:** Permite predecir si los versos de un nuevo poema son alejandrinos o no.

## Librerías Requeridas

Este proyecto requiere las siguientes librerías:

- `numpy` para operaciones numéricas y manipulación de arreglos.
- `tensorflow` para crear y entrenar el modelo LSTM.
- `pandas` para manipulación de datos.
- `re` para procesamiento de texto con expresiones regulares.

### Instalación de Dependencias

Puedes instalar las librerías necesarias utilizando `pip`. Asegúrate de tener `pip` actualizado y ejecuta los siguientes comandos:

```bash
pip install numpy pandas tensorflow
```

## Uso

1. **Preparar el Archivo CSV:** Asegúrate de tener un archivo CSV (`poems.csv`) con una columna llamada `content` que contenga los poemas.

2. **Ejecutar el Script:** Ejecuta el script de Python que realiza la carga de datos, entrenamiento del modelo y predicción.

3. **Ejemplo de Predicción:** Puedes probar el modelo con un poema nuevo como se muestra a continuación:

    ```python
    nuevo_poema = "La princesa está triste… ¿qué tendrá la princesa?\nEl viento de la noche gira en el cielo y canta"
    print(predecir_alejandrino(nuevo_poema))
    ```

## Detalles del Código

### Función `contar_silabas(verso)`

Cuenta el número de sílabas en un verso considerando diptongos y sinalefas.

### Función `es_alejandrino(silabas)`

Verifica si el número de sílabas en un verso es igual a 14.

### Construcción del Modelo LSTM

1. **Capa de Embeddings:** Representa palabras en un espacio vectorial denso.
2. **Capa LSTM:** Captura la dependencia temporal en el texto.
3. **Capa Densa:** Proporciona la salida final con activación sigmoide para clasificación binaria.

### Entrenamiento del Modelo

El modelo se entrena con un 80% de los datos para entrenamiento y un 20% para validación durante 10 épocas.

## Contribuciones

Si deseas contribuir al proyecto, por favor, abre un issue o una solicitud de extracción (pull request) con tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.