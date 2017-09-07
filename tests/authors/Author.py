import codecs

class Author:

    def __init__(self, author_path):
        content = []
        with codecs.open(author_path, 'r', encoding='utf-8') as f:
            content = list(map(lambda str: str.strip(), f.readlines()))

        self.name = content[0]
        self.language = content[1].lower()
        self.quotes = content[3:]
