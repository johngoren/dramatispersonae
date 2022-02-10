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

def is_mentioned_elsewhere_in_longer_form(name, all_names):
    for x in all_names:
        if is_same_name_in_longer_form(x, name):
            return True
    return False

def is_same_name_in_longer_form(label, name):
    if label is not name:

        if name in label:
            return True
    return False


def get_first_mention(name):
    # TODO: Extract first sentence mentioning the person, and add it to our dramatis personae.
    # TODO: More advanced ML version will turn the sentence into a capsule bio.
    pass

def merge_later_mentions(names):
    return [x for x in names if not is_mentioned_elsewhere_in_longer_form(x, names)]     

example = get_example()
nlp_entries = nlp(example)
tuples = [(X.text, X.label_) for X in nlp_entries.ents]
just_people = set(filter(is_person, tuples))
flat_list = [entry[__LABEL__] for entry in just_people]
print(flat_list)

merged_last_names = merge_later_mentions(flat_list)
print(merged_last_names)
