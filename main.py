import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")


def get_example():
    with open('./assets/breslin.txt', 'r') as file:
        data = file.read()
        return data

def is_person(entry):
    type = entry[1]
    if type == "PERSON":
        return True
    return False

example = get_example()
nlp_entries = nlp(example)
tuples = [(X.text, X.label_) for X in nlp_entries.ents]
just_people = filter(is_person, tuples)

print(set(just_people))

# print([(X.text, X.label_) for X in nlp_entries.ents])

# filtered_for_people = filter(is_person, nlp_entries)
# people = list(filtered_for_people)
# print(people)

