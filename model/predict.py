import numpy as np
import pandas as pd
import string
import pickle
from typing import Dict, Union

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

# load pre-tranined tokenizer
with open('model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load pre-trained model
len_max = 48
model = tf.keras.models.load_model('model/model.h5')

lemmatizer = WordNetLemmatizer()

def give_sig(scores: np.ndarray, used_text: str) -> Dict[str, Union[str, float]]:
    max_prob_pos = np.array(scores).argmax()
    if(max_prob_pos == 2):
    	return {'text': used_text, 'result': 'neutral', 'accuracy': f"{scores[0][2]:.2f}"}
    elif(max_prob_pos > 2):
    	return {'text': used_text, 'result': 'positive', 'accuracy': f"{scores[0][3] + scores[0][4]:.2f}"}
    else:
    	return {'text': used_text, 'result': 'negative', 'accuracy': f"{scores[0][0] + scores[0][1]:.2f}"}

def predict(sentence: str) -> Dict[str, Union[str, float]]:
    sentence = lemmatizer.lemmatize(sentence.lower()).translate(str.maketrans('', '', string.punctuation)).split()
    # predict single sentence: need to put sentence into an array
    sentence = tokenizer.texts_to_sequences([sentence])
    sentence = pad_sequences(sentence, maxlen=len_max, padding="pre", truncating="pre")
    used_text = tokenizer.sequences_to_texts(sentence)[0]
    scores = model.predict(sentence)
    return give_sig(scores, used_text)
