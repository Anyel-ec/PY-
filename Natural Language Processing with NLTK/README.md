# Natural Language Processing with NLTK

Author: Isabel Segura Bedmar

This project uses the NLTK library to perform various natural language processing (NLP) tasks in Python. Comments have been added to the code to describe its functionality and help understand each step in detail. Below are the steps and code examples used in this project.

## 1. Installation and Resource Downloads

Before starting, it is necessary to download some resources and models required to perform specific NLP tasks with NLTK.

```python
import nltk

# Download the sentence tokenizer 'punkt'
nltk.download('punkt')

# Download the part-of-speech tagger 'averaged_perceptron_tagger'
nltk.download('averaged_perceptron_tagger')

# Download the 'wordnet' dataset for lemmatization
nltk.download('wordnet')

# Download the POS tagsets
nltk.download('tagsets')

# Download the chunker 'maxent_ne_chunker' for named entity recognition
nltk.download('maxent_ne_chunker')

# Download the words corpus needed for chunking
nltk.download('words')

# Download the list of stopwords
nltk.download('stopwords')
```

## 2. Tokenization

The text is divided into sentences and words using NLTK tokenizers. The comments in the code explain how tokenization works and the importance of these steps in text processing.

```python
import nltk

# Tokenize a text into sentences
text = '''Billy always listens to his mother. He always does what she says.'''
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    print(sentence)

# Tokenize a text into words
text = "Mr. O'Neill thinks that the boys' stories about Chile's capital aren't amusing."
tokens = nltk.word_tokenize(text)
print(tokens)
```

## 3. Lemmatization and Stemming

The WordNet lemmatizer and the Porter stemmer are used to reduce words to their base form. The comments included in the code provide a clear understanding of the differences between lemmatization and stemming.

```python
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Lemmatization
word = 'better'
print(word, ",  lemma:", lematizer.lemmatize(word, 'a'))

# Stemming
print(word, " stem:", stemmer.stem(word))

# Additional examples of lemmatization and stemming
for word in ['easy', 'easily', 'easier', 'easiest']:
    print(word, ' stem=', stemmer.stem(word), " lemma:", lematizer.lemmatize(word, 'a'))
```

## 4. Stopword Removal

Stopwords are removed from the text to focus on the most relevant words. The comments in the code describe how this process is carried out and its usefulness in text analysis.

```python
from nltk.corpus import stopwords

# Load the stopwords in Spanish
stop_words = sorted(stopwords.words("spanish"))

# Tokenize the text and remove stopwords
text = 'El ajedrez es un juego de estrategia.'
tokens = nltk.word_tokenize(text)
relevant_tokens = [token for token in tokens if token.lower() not in stop_words]
print(relevant_tokens)
```

## 5. Part-of-Speech Tagging and Named Entity Recognition

Words are tagged with their grammatical categories, and named entity recognition (NER) is performed. The comments guide the reader in interpreting the tags and the results of the NER.

```python
import nltk

# Part-of-speech tagging
text = "Apple opened its first retail store in Mumbai on Tuesday."
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
print(tags)

# Named entity recognition (NER)
ner_tags = nltk.ne_chunk(tags)
print(ner_tags)
```

## 6. Stemming in Spanish

The Snowball stemmer is applied for the Spanish language. The comments explain how stemming is implemented in Spanish and the results you can expect.

```python
from nltk.stem import SnowballStemmer

# Create a SnowballStemmer instance for Spanish
sno = SnowballStemmer('spanish')

# Apply the stemmer to words in Spanish
for word in ['cantar', 'cantaré', 'cantaba', 'cantó', 'cantaron']:
    print(word, 'stem=', sno.stem(word))
```

## Rights

This material is the intellectual property of Universidad Carlos III de Madrid. Usage, copying, and distribution of this material are permitted under the Creative Commons BY-NC-SA 4.0 license, provided that attribution is maintained and it is not used for commercial purposes.

<img align='right' src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" width=15%/>
