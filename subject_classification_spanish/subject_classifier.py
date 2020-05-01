
from keras.preprocessing.sequence import pad_sequences
from keras.models import model_from_json
from pathlib import Path
import re
import pickle
import numpy as np

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^\w\s]')
stopwords_imported = ['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este', 'sí', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os', 'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 'está', 'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén', 'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría', 'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas', 'estábamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses', 'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habéis', 'han', 'haya', 'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá', 'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais', 'habrían', 'había', 'habías', 'habíamos', 'habíais', 'habían', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubiéramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiésemos', 'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seáis', 'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería', 'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras', 'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos', 'fueseis', 'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos', 'sentidas', 'siente', 'sentid', 'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan', 'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis', 'tendrán', 'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía', 'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened']
STOPWORDS = set(stopwords_imported)


class SubjectClassifier:
    def __init__(self, use_main_tags_only=False):
        self.maxlen = 700
        self.tokenizer = None
        self.multilabel_binarizer = None
        self.parent_path = Path(__file__).parent
        self.default_threshold = 0.001
        if (use_main_tags_only==True):
            self.path_tokenizer = 'saved_model/tokenizer_main_tags.pickle'
            self.path_binarizer = 'saved_model/multilabel_binarizer_main_tags.pickle'
            self.path_model_json = 'saved_model/model_main_tags.json'
            #self.path_model_h5 = "saved_model/model_main_tags.h5"
            self.path_model_h5 = "saved_model/model_main_tags.h5"
        else:
            self.path_tokenizer = 'saved_model/tokenizer.pickle'
            self.path_binarizer = 'saved_model/multilabel_binarizer.pickle'
            self.path_model_json = 'saved_model/model.json'
            self.path_model_h5 =    "saved_model/model.h5"

        with open(self.parent_path / self.path_tokenizer, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        # load categories
        with open(self.parent_path / self.path_binarizer, 'rb') as handle:
            self.multilabel_binarizer = pickle.load(handle)

        # load json and create model
        json_model_keras = open(self.parent_path / self.path_model_json, 'r')
        loaded_model_json = json_model_keras.read()
        json_model_keras.close()
        self.loaded_model = model_from_json(loaded_model_json)

        # load weights into new model
        self.loaded_model.load_weights(self.parent_path / self.path_model_h5)

        # evaluate loaded model on test data
        self.loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def clean_text(self, text):
            text = text.lower() # lowercase text
            text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
            text = BAD_SYMBOLS_RE.sub('', text) # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing. 
            #    text = re.sub(r'\W+', '', text)
            STOPWORDS.add("\n")
            text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove stopwors from text
            text = text.strip()
            return text

    def obtain_classes(self, proba, default_threshold, limit=10):
        idxs = np.argsort(proba)[::-1][:limit]
        subjects = dict()
        # loop over the indexes of the high confidence class labels
        for (i, j) in enumerate(idxs):
            if (proba[j] > default_threshold):
                # build the label and draw the label on the image
                subject = self.multilabel_binarizer.classes_[j]
                probability = proba[j]
                subjects[subject] = probability
        return subjects
                
    #returns the sentiment of a text string
    def classify(self, text:str, **kwargs):
        default_threshold = self.default_threshold
        limit = 10
        if ("default_threshold" in kwargs):
            default_threshold = kwargs.get("default_threshold")
        if ("limit" in kwargs):
            limit = kwargs.get("limit")
        x = self.tokenizer.texts_to_sequences([self.clean_text(text)])
        x = pad_sequences(x, padding='post', maxlen=self.maxlen)

        y_new = self.loaded_model.predict(x)
        return self.obtain_classes(y_new[0], default_threshold, limit)


    def obtain_raw_probabilities(self, text:str):
        x = self.tokenizer.texts_to_sequences([self.clean_text(text)])
        x = pad_sequences(x, padding='post', maxlen=self.maxlen)
        return self.loaded_model.predict(x)

