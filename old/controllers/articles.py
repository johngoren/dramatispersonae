
def get_frank_sinatra_sample():
    with open('./assets/talese.txt', 'r') as file:
        data = file.read()
        return clean_article(data)
    
def clean_article(article):
    return article.replace("'s", "") # TODO: Fix newlines