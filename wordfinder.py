"""Word Finder: finds random words from a dictionary."""

import random 


class WordFinder:
    """find random words from dictionary"""

    def __init__(self,path):

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")
