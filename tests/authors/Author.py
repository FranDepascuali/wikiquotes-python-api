from io import open

class Author:

    def __init__(self, author_path):
        content = []
        with open(author_path, 'r', encoding="utf-8") as f:
            content = list(map(lambda sentence: sentence.strip(), f.readlines()))

        self.name = content[0]
        self.language = content[1]
        self.quotes = content[3:]
