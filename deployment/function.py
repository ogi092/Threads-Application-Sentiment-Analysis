"""
Ogi Hadicahyo

Objective: creating a specific file to call the functions used
"""
import pandas as pd
import numpy as np
# preprocess
import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import joblib

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
stopword_list= joblib.load('stopword_list.joblib')

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()          # Define Lemmatizer
    text = text.lower()                       # Lowercase text
    text = text.strip()
    text = re.sub("[^A-Za-z\s']", "", text)  # Non-letter removal (such as emoticon, symbol (like μ, $, 兀), etc
    tokens = word_tokenize(text)              # Tokenize
    filtered_words = [word for word in tokens if word not in stopword_list]        # Stopwords Removal
    lemmatized_words = [lemmatizer.lemmatize(w) for w in filtered_words]        # Changing words to their basic form (lemmatization)
    lemmatized_clean = [word.translate(str.maketrans('', '', string.punctuation)) for word in lemmatized_words] # Cleans the text from punctuation marks
    return ' '.join(lemmatized_clean)

def prediction(X):
    model = load_model('best_model.keras')
    y_pred = model.predict(X)
    predictions = np.argmax(y_pred, axis=1)
    for val in predictions:
        if val == 0:
            return 0, f"Text indicates the person is giving **Positive** sentiment"
        elif val == 1:
            return 1, f"Text indicates the person is giving **Negative** sentiment"
        else:
            return 2, f"Text indicates the person is giving **Neutral** sentiment"