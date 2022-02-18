import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('sentencizer')

from constants import __LABEL__, __TYPE__

aliases = {}


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

def prep_article_for_parsing(article):
    return article

    # prepped = article.replace("'s", "")    # Possessives are tricky
    # return prepped