
def get_joan_didion_sample():
    with open('./assets/didion.txt', 'r') as file:
        data = file.read()
        return clean_article(data)
    
def clean_article(article):
    return article # TODO: Fix newlines