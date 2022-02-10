import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")


def get_example():
    with open('./assets/breslin.txt', 'r') as file:
        data = file.read()
        return data

example = get_example()
doc = nlp(example)

print([(X.text, X.label_) for X in doc.ents])


