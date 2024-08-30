# spaCy NLP Examples

Este repositorio contiene ejemplos básicos de procesamiento de lenguaje natural (NLP) utilizando la biblioteca `spaCy`. A continuación se detallan los scripts y visualizaciones implementados.

## Instalación

Para instalar `spaCy`, puedes usar el siguiente comando:

```bash
!pip install -q spacy
```

## Cargando Modelos de spaCy

El modelo de lenguaje en inglés `en_core_web_sm` se carga de la siguiente manera:

```python
import spacy
model = spacy.load('en_core_web_sm')
```

Otra forma alternativa de cargar el modelo es:

```python
import en_core_web_sm
nlp = en_core_web_sm.load()
```

## Procesamiento de Texto

### Ejemplo de Texto

```python
text = '''Pedro Sánchez Pérez-Castejón (born 29 February 1972) is a Spanish politician
who has been Prime Minister of Spain since June 2018.'''
document = model(text)
```

### Análisis de Oraciones

Itera sobre las oraciones y las imprime:

```python
for i, s in enumerate(document.sents):
    print("Sentence:", s)
    print("Entities:")
    for e in s.ents:
        print('\t', e.text, e.label_, e.start_char, e.end_char)
    print()
```

### Análisis de Tokens

Itera sobre cada token en el documento y extrae varias propiedades:

```python
for token in doc:
    print("word:", token.orth_)
    print("grammatical relation:", token.dep_)
    print("connected word (head):", token.head.orth_)
    print('------------------------------------------')
```

### Visualización de Dependencias Gramaticales

Para visualizar las relaciones gramaticales de una oración:

```python
from spacy import displacy
displacy.render(doc, jupyter=True, style='dep')
```

### Visualización de Entidades Nombradas

Para visualizar las entidades nombradas en el texto:

```python
displacy.render(document, jupyter=True, style='ent')
```

## Ejemplos de Código

1. **Iteración sobre oraciones y extracción de entidades:**

```python
for i, s in enumerate(document.sents):
    print("Sentence:", s)
    print("Entities:")
    for e in s.ents:
        print('\t', e.text, e.label_, e.start_char, e.end_char)
    print()
```

2. **Visualización de dependencias:**

```python
displacy.render(doc, jupyter=True, style='dep')
```

3. **Visualización de entidades nombradas:**

```python
displacy.render(document, jupyter=True, style='ent')
```

## Visualización Gráfica

### Árbol de Dependencias Gramaticales

![Dependencias Gramaticales](ruta_a_la_imagen_del_arbol)

### Entidades Nombradas

![Entidades Nombradas](ruta_a_la_imagen_de_entidades)

## Conclusión

Este proyecto demuestra cómo utilizar `spaCy` para realizar análisis de texto, desde la identificación de dependencias gramaticales hasta la visualización de entidades nombradas. Los ejemplos proporcionados son un punto de partida para explorar más capacidades avanzadas de `spaCy` en proyectos de NLP.

## Derechos

- Derechos a: Universidad Carlos III de Matrix
- Autora: Isabel Segura Bedmar
