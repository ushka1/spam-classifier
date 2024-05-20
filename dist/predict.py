import json
import os
import pickle
import string
import sys

import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


def text_transform(text: str) -> str:
    result = text.lower()
    result = nltk.word_tokenize(result)

    temp = []
    for word in result:
        if word.isalnum():
            temp.append(word)
    result = temp

    temp = []
    for word in result:
        if word not in nltk.corpus.stopwords.words('english') and word not in string.punctuation:
            temp.append(word)
    result = temp

    temp = []
    for word in result:
        temp.append(stemmer.stem(word))
    result = temp

    return " ".join(result)


current_path = os.path.dirname(os.path.realpath(__file__))
vectorizer_path = os.path.join(current_path, 'vectorizer.pkl')
model_path = os.path.join(current_path, 'classifier.pkl')

tfidf = pickle.load(open(vectorizer_path, 'rb'))
model = pickle.load(open(model_path, 'rb'))


# ----------------------------------------

input_data = sys.argv[1]
transformed_data = text_transform(input_data)
vectorized_data = tfidf.transform([transformed_data])
result = model.predict(vectorized_data)

print(result[0])
