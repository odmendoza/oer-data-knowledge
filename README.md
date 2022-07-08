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

```
__label__ http://oasis.col.org/handle/11599/2562 entrepreneurship 
__label__ http://oasis.col.org/handle/11599/2562 flexible learning 
__label__ http://oasis.col.org/handle/11599/2562 inclusive education
```

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

## app.py

Se trata de una aplicación de [Flask](https://flask.palletsprojects.com/en/1.1.x/) con dos vistas:

- index
```python
@app.route('/')
def index():
    session = init_db()
    tripletes = session.query(Triplete).filter(Triplete.predicate == 'title')
    return render_template('index.html', tripletes=tripletes)
```
Esta vista lo que haces es abrir una conección con la base de datos, traer los 
registros de las tripletas dond el predicado sea el título. (Se puede mejorar, depende 
de lo que se quiera mostrar). En el index, con un __for__ se muestra las tripletas.

- prediction
```python
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        search = request.form['search']
        # Preprocesar entrada de texto
        result = Prediction
        search = Preprocessing.pre_process(search)
        p = result.predicty(search)
        print(p)
        tripletes = []
        session = init_db()
        for i in p[0] :
            i = i.replace('__label__', '')
            i = i.replace('-', ' ')
            i += '?show=full'
            aux = session.query(Triplete).filter(Triplete.predicate == 'title')
            print(aux)
            for a in aux :
                if a.subject == i :
                    tripletes.append(a)
            print(i)
    return render_template('index.html', tripletes=tripletes)
```

Esta vista se activa cuando el usuario realiza una búsqueda 
mediante un formulario. Se preprocesa la entrada de texto 
para que la predicción sea lo más acertada posible. (Esto debido a 
que el resultado de la predicción varía si se usa palabras en 
mayúsculas o minúsculas o con números, por ejemplo).

Después se abre una conexión con la base de datos y se trae de 
nuevo todas las tripletas que tengan como predicado el título del 
recurso, que es lo que se desea mostrar. Pero solo se envía al template 
aquellas que coinciden con el resultado de la predicción _p = result.predicty(search)_
