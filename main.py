import spacy
from spacy import displacy
from collections import Counter
from spacy.lang.en import English
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('sentencizer')

__LABEL__ = 0
__TYPE__ = 1

aliases = {}

def get_example():
    with open('./assets/talese.txt', 'r') as file:
        data = file.read()
        return clean_article(data)
    
def clean_article(article):
    return article # TODO: Fix newlines

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
            aliases[name] = label
            return True
    return False

def is_same_name_as_possessive(label, name):
    # TODO
    pass

def get_first_mention(sentences, name):
    for sentence in sentences:
        if name in sentence:
            return (name, sentence)

    # TODO: More advanced ML version will turn the sentence into a capsule bio.

def merge_later_mentions(names):
    return [x for x in names if not is_mentioned_elsewhere_in_longer_form(x, names)]     

def split_into_sentences(text):
    doc = nlp(text)
    return [str(sent).strip() for sent in doc.sents]



article = get_example()
nlp_entries = nlp(article)
tuples = [(X.text, X.label_) for X in nlp_entries.ents]
just_people = set(filter(is_person, tuples))
flat_list = [entry[__LABEL__] for entry in just_people]
merged_last_names = merge_later_mentions(flat_list)
print(merged_last_names)

sentences = split_into_sentences(article)
first_mentions = [get_first_mention(sentences, x) for x in merged_last_names]

print(aliases)