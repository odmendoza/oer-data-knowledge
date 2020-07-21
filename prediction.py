import fasttext
import string
import stanfordnlp

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


class Prediction():

    def predicty(text) :
        model = fasttext.load_model('./models/text-classification-model.bin')
        prediction = model.predict(text=text, k=-1, threshold=0.01)
        return prediction


class Preprocessing():
    def pre_process(text):
        nlp = stanfordnlp.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')
        sw = stopwords.words('english')
        # Token
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
                    # Lemma
                    aux += word.lemma
                    aux += ' '
            s.append(aux)
        return ' '.join(s)
