import os
import pickle
import string
import sys

import nltk
from nltk.stem.porter import PorterStemmer


current_path = os.path.dirname(os.path.realpath(__file__))
vectorizer_path = os.path.join(current_path, 'vectorizer.pkl')
model_path = os.path.join(current_path, 'classifier.pkl')

vectorizer = pickle.load(open(vectorizer_path, 'rb'))
model = pickle.load(open(model_path, 'rb'))

# ----------------------------------------

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


# ----------------------------------------


def make_prediction(input_data: str) -> str:
    transformed_data = text_transform(input_data)
    vectorized_data = vectorizer.transform([transformed_data])
    result = model.predict(vectorized_data)

    return result[0]


input_data = sys.argv[1]
result = make_prediction(input_data)
print(result)
