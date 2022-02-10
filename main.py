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

def get_first_mention(name):
    # TODO: Extract first sentence mentioning the person, and add it to our dramatis personae.
    # TODO: More advanced ML version will turn the sentence into a capsule bio.
    pass

def merge_equivalents(names):
    # TODO: Merge items that contain other items, like last names duplicated by full names.
    return names

example = get_example()
nlp_entries = nlp(example)
tuples = [(X.text, X.label_) for X in nlp_entries.ents]
just_people = set(filter(is_person, tuples))
merged_equivalents = merge_equivalents(just_people)

# TODO: 
print(set(merged_equivalents))

# print([(X.text, X.label_) for X in nlp_entries.ents])

# filtered_for_people = filter(is_person, nlp_entries)
# people = list(filtered_for_people)
# print(people)

