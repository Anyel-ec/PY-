# Importación de librerías necesarias
import numpy as np  # Para operaciones numéricas y manipulación de arreglos
from tensorflow.keras.preprocessing.text import Tokenizer  # Para tokenizar el texto (convertir palabras en números)
from tensorflow.keras.preprocessing.sequence import pad_sequences  # Para rellenar secuencias a una longitud fija
from tensorflow.keras.models import Sequential  # Para crear un modelo secuencial en Keras
from tensorflow.keras.layers import Embedding, LSTM, Dense  # Capas necesarias para el modelo LSTM
import pandas as pd  # Para manipulación de datos
import re  # Para expresiones regulares, útil para procesar texto

# Función mejorada para contar sílabas en un verso
def contar_silabas(verso)
    # Convierte el verso a minúsculas y elimina espacios en blanco al inicio y final
    verso = verso.lower().strip()

    # Encuentra todas las secuencias de dos vocales juntas (posibles diptongos o hiatos)
    diptongos_hiatos = re.findall(r'[aeiouáéíóúü]{2}', verso)
    # Cuenta todas las vocales en el verso
    silabas = len(re.findall(r'[aeiouáéíóúü]', verso))

    # Resta las sinalefas (vocal final de una palabra seguida de vocal inicial de la siguiente palabra)
    silabas -= len(re.findall(r'[aeiouáéíóúü]s+[aeiouáéíóúü]', verso))

    # Ajuste para los diptongos e hiatos
    for par in diptongos_hiatos
        if re.match(r'[aeiouáéíóúü]{2}', par)
            silabas -= 1  # Si es un diptongo, se cuenta como una sola sílaba

    return silabas  # Devuelve el número total de sílabas en el verso

# Función para verificar si un verso es alejandrino (14 sílabas)
def es_alejandrino(silabas)
    return silabas == 14  # Retorna True si el verso tiene 14 sílabas, False en caso contrario

# Cargar el archivo CSV
file_path = 'contentpoems.csv'  # Especifica la ruta al archivo CSV que contiene los poemas
df = pd.read_csv(file_path)  # Carga el archivo CSV en un DataFrame de pandas

# Filtrar solo la columna 'content' y remover valores nulos
poemas = df['content'].dropna()  # Selecciona la columna 'content' y elimina filas con valores nulos

# Tokenización y secuencias
tokenizer = Tokenizer(char_level=False)  # Crea un objeto Tokenizer para tokenizar el texto a nivel de palabras
tokenizer.fit_on_texts(poemas)  # Ajusta el tokenizer a los poemas
sequences = tokenizer.texts_to_sequences(poemas)  # Convierte los poemas en secuencias de enteros (tokens)
max_sequence_len = max([len(seq) for seq in sequences])  # Calcula la longitud máxima de las secuencias

# Padding de las secuencias para que todas tengan la misma longitud
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_len, padding='post')  # Rellena las secuencias para que todas tengan la misma longitud

# Etiquetas 1 para alejandrino (14 sílabas), 0 para no alejandrino
labels = []  # Inicializa una lista para las etiquetas
for poema in poemas  # Itera sobre cada poema
    versos = poema.split('n')  # Divide el poema en versos (líneas) por el salto de línea
    for verso in versos  # Itera sobre cada verso
        if verso.strip()  # Verifica que el verso no esté vacío
            silabas = contar_silabas(verso)  # Cuenta las sílabas en el verso
            labels.append(1 if es_alejandrino(silabas) else 0)  # Añade 1 si el verso es alejandrino, 0 en caso contrario

# Convertir etiquetas a numpy array
labels = np.array(labels)  # Convierte la lista de etiquetas a un array de numpy

# Construcción del modelo LSTM
vocab_size = len(tokenizer.word_index) + 1  # Tamaño del vocabulario (número total de palabras únicas en los poemas)
embedding_dim = 128  # Dimensión de los embeddings (representación densa de las palabras)
lstm_units = 100  # Número de unidades en la capa LSTM

model = Sequential()  # Inicia un modelo secuencial
model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_sequence_len))  # Añade una capa de embeddings
model.add(LSTM(lstm_units, return_sequences=False))  # Añade una capa LSTM
model.add(Dense(1, activation='sigmoid'))  # Añade una capa densa con activación sigmoide para la salida

# Compilación del modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])  # Compila el modelo con pérdida binaria y optimizador Adam

# Entrenamiento del modelo
model.fit(padded_sequences, labels, epochs=10, validation_split=0.2, batch_size=32)  # Entrena el modelo durante 10 épocas con un batch size de 32 y validación del 20%

# Ejemplo de predicción con un poema nuevo
def predecir_alejandrino(poema)
    versos = poema.split('n')  # Divide el poema en versos (líneas)
    secuencia_poema = tokenizer.texts_to_sequences([poema])  # Tokeniza el poema en secuencia de enteros
    secuencia_poema_padded = pad_sequences(secuencia_poema, maxlen=max_sequence_len, padding='post')  # Aplica padding a la secuencia del poema
    prediccion = model.predict(secuencia_poema_padded)  # Predice si el poema es alejandrino o no

    resultados = []  # Lista para almacenar los resultados
    for i, verso in enumerate(versos)  # Itera sobre cada verso del poema
        silabas = contar_silabas(verso)  # Cuenta las sílabas en el verso
        es_alej = es_alejandrino(silabas)  # Verifica si el verso es alejandrino
        resultados.append(Alejandrino if es_alej else No alejandrino)  # Añade el resultado a la lista

    return resultados  # Devuelve la lista de resultados

# Ejemplo de uso
nuevo_poema = La princesa está triste… ¿qué tendrá la princesanEl viento de la noche gira en el cielo y canta  # Poema de ejemplo
print(predecir_alejandrino(nuevo_poema))  # Imprime los resultados de la predicción
