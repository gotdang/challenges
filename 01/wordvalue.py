"""Read in dictionary.txt (a copy of /usr/share/dict/words on my Mac) and 
calculate the word that has the most value in Scrabble based on LETTER_SCORES 
which is imported in wordvalue-template.py."""
from data import DICTIONARY, LETTER_SCORES

def memoize(f):
    class memodict(dict):
        __slots__ = ()
        def __missing__(self, key):
            self[key] = ret = f(key)
            return ret
    return memodict().__getitem__

def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__


def load_words(input_file = DICTIONARY):
    """Load dictionary into a list and return list"""
    with open(input_file, "r") as wordfile:
        return list((word for word in wordfile.read().split("\n") if word))


@memoize
def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum( [LETTER_SCORES.get(letter, 0) for letter in word.upper()] )


def max_word_value(arg = load_words(DICTIONARY)):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY """
    return max(((calc_word_value(word), word) for word in arg))[1]


if __name__ == "__main__":
    pass # run unittests to validate
