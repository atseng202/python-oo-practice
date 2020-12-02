from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        """ Creates a WordFinder instance with a path to a file on disk 
        that contains words, one word per line """
        self.file_path = file_path
        self.words = self.get_words()
        self.words_read()

    def get_words(self):
        """ Opens file to read and returns a list of those words in file """
        file = open(self.file_path, "r")
        words = [line.strip() for line in file if self.is_valid_word(line)]
        file.close()
        return words

    def is_valid_word(self, line):
        """ No filter for normal word list. Always True """
        return True
        # raise NotImplementedError

    def words_read(self):
        """ Prints out number of words read """
        print(f"{len(self.words)} words read")

    def random(self):
        """ Returns a random word from that list of words """
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """ WordFinder subclass that returns only words in the file, 
    but never returns blank lines or comments """

    def is_valid_word(self, line):
        """ Takes in the line and returns boolean.
            Returns true if line is a word 
            Returns false if line is blank or comment """

        return bool(line.strip() and (not line.startswith('#')))
