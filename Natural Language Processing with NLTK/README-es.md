# Procesamiento de Lenguaje Natural con NLTK

Autora: Isabel Segura Bedmar

Este proyecto utiliza la biblioteca NLTK para realizar diversas tareas de procesamiento de lenguaje natural (PLN) en Python. Se han agregado comentarios en el código para describir su funcionamiento y ayudar a comprender cada paso en detalle. A continuación, se describen los pasos y ejemplos de código utilizados en este proyecto.

## 1. Instalación y Descarga de Recursos

Antes de comenzar, es necesario descargar algunos recursos y modelos necesarios para realizar tareas específicas de PLN con NLTK.

```python
import nltk

# Descargar el tokenizador de frases 'punkt'
nltk.download('punkt')

# Descargar el etiquetador gramatical 'averaged_perceptron_tagger'
nltk.download('averaged_perceptron_tagger')

# Descargar el conjunto de datos 'wordnet' para lematización
nltk.download('wordnet')

# Descargar el conjunto de etiquetas gramaticales 'tagsets'
nltk.download('tagsets')

# Descargar el chunker 'maxent_ne_chunker' para reconocimiento de entidades nombradas
nltk.download('maxent_ne_chunker')

# Descargar el corpus de palabras necesario para el chunker
nltk.download('words')

# Descargar la lista de palabras de parada (stopwords)
nltk.download('stopwords')
```

## 2. Tokenización

Se divide un texto en oraciones y palabras utilizando los tokenizadores de NLTK. Los comentarios en el código explican cómo funciona la tokenización y la importancia de estos pasos en el procesamiento de texto.

```python
import nltk

# Tokenizar un texto en oraciones
text = '''Billy always listens to his mother. He always does what she says.'''
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    print(sentence)

# Tokenizar un texto en palabras
text = "Mr. O'Neill thinks that the boys' stories about Chile's capital aren't amusing."
tokens = nltk.word_tokenize(text)
print(tokens)
```

## 3. Lematización y Stemming

Se utiliza el lematizador de WordNet y el stemmer de Porter para reducir las palabras a su forma base. Los comentarios incluidos en el código proporcionan una comprensión clara de las diferencias entre lematización y stemming.

```python
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Lematización
word = 'better'
print(word, ",  lema:", lematizer.lemmatize(word, 'a'))

# Stemming
print(word, " stem:", stemmer.stem(word))

# Ejemplos adicionales de lematización y stemming
for word in ['easy', 'easily', 'easier', 'easiest']:
    print(word, ' stem=', stemmer.stem(word), " lema:", lematizer.lemmatize(word, 'a'))
```

## 4. Eliminación de Palabras de Parada

Se eliminan las palabras de parada (stopwords) del texto para centrarse en las palabras más relevantes. Los comentarios en el código describen cómo se realiza este proceso y su utilidad en análisis de texto.

```python
from nltk.corpus import stopwords

# Cargar las stopwords en español
stop_words = sorted(stopwords.words("spanish"))

# Tokenizar el texto y eliminar stopwords
text = 'El ajedrez es un juego de estrategia.'
tokens = nltk.word_tokenize(text)
relevant_tokens = [token for token in tokens if token.lower() not in stop_words]
print(relevant_tokens)
```

## 5. Etiquetado Gramatical y Reconocimiento de Entidades Nombradas

Se etiquetan las palabras con sus categorías gramaticales y se realiza el reconocimiento de entidades nombradas (NER). Los comentarios guían al lector en la interpretación de las etiquetas y los resultados del NER.

```python
import nltk

# Etiquetado gramatical
text = "Apple opened its first retail store in Mumbai on Tuesday."
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
print(tags)

# Reconocimiento de entidades nombradas (NER)
ner_tags = nltk.ne_chunk(tags)
print(ner_tags)
```

## 6. Stemming en Español

Se aplica el stemmer de Snowball para el idioma español. Los comentarios explican cómo se implementa el stemming en español y los resultados que se pueden esperar.

```python
from nltk.stem import SnowballStemmer

# Crear una instancia de SnowballStemmer para español
sno = SnowballStemmer('spanish')

# Aplicar el stemmer a palabras en español
for word in ['cantar', 'cantaré', 'cantaba', 'cantó', 'cantaron']:
    print(word, 'stem=', sno.stem(word))
```

## Derechos

Este material es propiedad intelectual de la Universidad Carlos III de Madrid. Se permite el uso, copia y distribución de este material bajo la licencia Creative Commons BY-NC-SA 4.0, siempre y cuando se mantenga la atribución y no se utilice para fines comerciales.

<img align='right' src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" width=15%/>