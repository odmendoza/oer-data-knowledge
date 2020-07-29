# OER DATA KNOWLEDGE

OER DATA KNOWLEDGE es una pequeña aplicación que implementa un 
clasificador de texto con [FastText](https://fasttext.cc/) y Python.

## Los archivos del proyecto que interesan son

- templates/
    - base.html
    - index.html
- app.py
- data.train
- model_building.py
- prediction.py
- models.py

## Los datos (data.train)

Los datos de la Base de conocimiento deben encontarse en formato [etiqueta] [valor] [Más información](https://fasttext.cc/docs/en/supervised-tutorial.html). Por ejemplo:

__label__http://oasis.col.org/handle/11599/2562 entrepreneurship 
__label__http://oasis.col.org/handle/11599/2562 flexible learning 
__label__http://oasis.col.org/handle/11599/2562 inclusive education

La etiqueta debe siempre empezar con '_ _ _label_ _ _', y seguido de un espacio, el valor.

## Creación de modelos

Crear un modelo

```python
import fasttext as ft
model = ft.train_supervised(input="data.train",
                            lr=0.45,
                            epoch=200,
                            wordNgrams=2,
                            ws=5,
                            dim=100)
```

Más información sobre los parámetros, ver [aquí](https://fasttext.cc/docs/en/supervised-tutorial.html#word-n-grams).

Guardar un modelo. Es una convención utilizar la extensión .bin

```python
model.save_model("./models/text-classification-model.bin")
```

## prediction.py

Contiene dos clases

- Prediction, con el método predicty() que recibe como parámetro el texto que va a predecir,
carga el modelo desde la ruta donde se guardó y devuelve la predicción.

```python
class Prediction():
    def predicty(text) :
        model = fasttext.load_model('./models/text-classification-model.bin')
        prediction = model.predict(text=text, k=-1, threshold=0.01)
        return prediction
```

- Preprocessing, con el método pre_process() que recibe el texto que va a preprocesar 
(proceso que consiste en tokenización, lemmatización y eliminación de stopwords )
```python
class Preprocessing():
    def pre_process(text):
        nlp = stanfordnlp.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')
        sw = stopwords.words('english')
        # Tokenization
        table = str.maketrans('', '', string.punctuation)
        sen = word_tokenize(text)
        sen = [w.lower() for w in sen]
        stripped = [w.translate(table) for w in sen]
        sen = [word for word in stripped if word.isalpha()]
        doc = nlp(' '.join(sen))
        s = []
        for sentence in doc.sentences:
            aux = ''
            for word in sentence.words:
                # Delete stopwords
                if word.text not in sw:
                    # Lemmatization
                    aux += word.lemma
                    aux += ' '
            s.append(aux)
        return ' '.join(s)
```