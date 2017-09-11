from io import open

import directory
import file_manager

class Author:

    def __init__(self, author_path):
        content = []
        with open(author_path, 'r', encoding="utf-8") as f:
            content = list(map(lambda sentence: sentence.strip(), f.readlines()))

        self.name = content[0]
        self.language = content[1]
        self.quotes = content[3:]

def fetch_all_authors():
    author_paths = file_manager.list_absolute_files_with_extension(directory.authors_directory, ".txt")
    return list(map(Author, author_paths))

def random_author():
    import random
    return random.choice(fetch_all_authors())
