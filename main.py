import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

__LABEL__ = 0
__TYPE__ = 1

def get_example():
    with open('./assets/breslin.txt', 'r') as file:
        data = file.read()
        return data

def is_person(entry):
    type = entry[__TYPE__]
    if type == "PERSON":
        return True
    return False

def is_mentioned_elsewhere_in_longer_form(entries, name):
    for entry in entries:
        label = entry[__LABEL__]
        if label_is_same_name_in_longer_form(label, name):
            return True
    return False

def label_is_same_name_in_longer_form(label, name):
    if label is not name:
        if name in label:
            return True
    return False


def get_first_mention(name):
    # TODO: Extract first sentence mentioning the person, and add it to our dramatis personae.
    # TODO: More advanced ML version will turn the sentence into a capsule bio.
    pass

def merge_equivalents(names):
    # TODO: Merge items that contain other items, like last names duplicated by full names.
    return set(filter(is_mentioned_elsewhere_in_longer_form, names))    

example = get_example()
nlp_entries = nlp(example)
tuples = [(X.text, X.label_) for X in nlp_entries.ents]
just_people = set(filter(is_person, tuples))
merged_equivalents = [entry for entry in just_people if is_mentioned_elsewhere_in_longer_form(entry, just_people) is False]

# TODO: 
print(merged_equivalents)

# print([(X.text, X.label_) for X in nlp_entries.ents])

# filtered_for_people = filter(is_person, nlp_entries)
# people = list(filtered_for_people)
# print(people)

