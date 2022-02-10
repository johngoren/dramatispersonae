
def get_example():
    with open('./assets/talese.txt', 'r') as file:
        data = file.read()
        return clean_article(data)
    
def clean_article(article):
    return article # TODO: Fix newlines