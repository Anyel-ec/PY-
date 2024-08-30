# spaCy NLP Examples

This repository contains basic examples of natural language processing (NLP) using the `spaCy` library. The following sections detail the scripts and visualizations implemented.

## Installation

To install `spaCy`, you can use the following command:

```bash
!pip install -q spacy
```

## Loading spaCy Models

The English language model `en_core_web_sm` is loaded as follows:

```python
import spacy
model = spacy.load('en_core_web_sm')
```

An alternative way to load the model is:

```python
import en_core_web_sm
nlp = en_core_web_sm.load()
```

## Text Processing

### Example Text

```python
text = '''Pedro Sánchez Pérez-Castejón (born 29 February 1972) is a Spanish politician
who has been Prime Minister of Spain since June 2018.'''
document = model(text)
```

### Sentence Analysis

Iterate over the sentences and print them:

```python
for i, s in enumerate(document.sents):
    print("Sentence:", s)
    print("Entities:")
    for e in s.ents:
        print('\t', e.text, e.label_, e.start_char, e.end_char)
    print()
```

### Token Analysis

Iterate over each token in the document and extract various properties:

```python
for token in doc:
    print("word:", token.orth_)
    print("grammatical relation:", token.dep_)
    print("connected word (head):", token.head.orth_)
    print('------------------------------------------')
```

### Dependency Visualization

To visualize the grammatical relations of a sentence:

```python
from spacy import displacy
displacy.render(doc, jupyter=True, style='dep')
```

### Named Entity Visualization

To visualize the named entities in the text:

```python
displacy.render(document, jupyter=True, style='ent')
```

## Code Examples

1. **Iteration over sentences and extraction of entities:**

```python
for i, s in enumerate(document.sents):
    print("Sentence:", s)
    print("Entities:")
    for e in s.ents:
        print('\t', e.text, e.label_, e.start_char, e.end_char)
    print()
```

2. **Dependency visualization:**

```python
displacy.render(doc, jupyter=True, style='dep')
```

3. **Named entity visualization:**

```python
displacy.render(document, jupyter=True, style='ent')
```

## Conclusion

This project demonstrates how to use `spaCy` to perform text analysis, from identifying grammatical dependencies to visualizing named entities. The examples provided serve as a starting point for exploring more advanced `spaCy` capabilities in NLP projects.

## Rights

- Rights to: Universidad Carlos III de Matrix
- Author: Isabel Segura Bedmar
