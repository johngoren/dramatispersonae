import spacy
from spacy import displacy
from collections import Counter
from spacy.lang.en import English
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('sentencizer')
import articles
from textUtils import is_person, merge_later_mentions, split_into_sentences, get_first_mention, aliases
from constants import __LABEL__, __TYPE__

article = articles.get_frank_sinatra_sample().replace(",","")
nlp_entries = nlp(article)
tuples = [(X.text, X.label_) for X in nlp_entries.ents]
just_people = list(filter(is_person, tuples))
flat_list = [entry[__LABEL__] for entry in just_people]
merged_last_names = merge_later_mentions(flat_list)
print("List of people")
print(merged_last_names)

sentences = split_into_sentences(article)
first_mentions = [get_first_mention(sentences, x) for x in merged_last_names]

print("Aliases")
print(aliases)

print("First mentions")

#for x in first_mentions:
#    name = x[0]
#    mention = x[1]
#    print(f'{name}: {mention}')
    
