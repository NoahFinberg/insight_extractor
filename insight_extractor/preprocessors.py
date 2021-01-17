import pandas as pd
import numpy as np

import os
import re
import string
from nltk.corpus import stopwords

import tensorflow as tf
from sklearn.model_selection import train_test_split

import json
from keras_preprocessing.text import tokenizer_from_json


### CONFIG ###
MAX_SEQ_LENGTH    = 500

def clean_doc(doc):
    """
    Cleaning a document by several methods:
        - Lowercase
        - Removing whitespaces
        - Removing numbers
        - Removing stopwords
        - Removing punctuations
        - Removing short words
    """
    stop_words = set(stopwords.words('english'))
    
    # Lowercase
    doc = doc.lower()
    # Remove numbers
    #doc = re.sub(r"[0-9]+", "", doc)
    # Split in tokens
    tokens = doc.split()
    # Remove Stopwords
    tokens = [w for w in tokens if not w in stop_words]
    # Remove punctuation
    tokens = [w.translate(str.maketrans('', '', string.punctuation)) for w in tokens]
    # Tokens with less then two characters will be ignored
    tokens = [word for word in tokens if len(word) > 1]
    return ' '.join(tokens)

# takes a list of sentences and cleans them
def clean_docs(docs):
    return [clean_doc(doc) for doc in docs]

# loads tokenizer from combined model training
# take a list of cleaned docs and returns them as a list of lists of tokenized words
def tokenize(docs, file):
    # load tokenizer
    with open(file) as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)

    sequences_test = tokenizer.texts_to_sequences(docs)
    tokenized_docs = tf.keras.preprocessing.sequence.pad_sequences(sequences_test, maxlen=MAX_SEQ_LENGTH, padding='post')
    return tokenized_docs