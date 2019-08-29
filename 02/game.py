#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
"""
We load in the necessary data structures to focus on the game:

# Note that DICTIONARY is a set for O(1) lookups
from data import DICTIONARY, LETTER_VALUES, POUCH
Draw 7 random letters from POUCH.

As said POUCH is given and contains a distribution of Scrabble letters so that 
the player gets enough vowels (equally drawing A-Z makes it extremely hard 
because you need more vowels to make words):

['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C',
'D', 'D', 'D', 'D', ...]
Ask the player to form a word with one or more of the 7 letters of the draw. 
Validate input for:

1) all letters of word are in draw;
2) word is in DICTIONARY.
Calculate the word value and show it to the player.

To focus on this challenge we re-use two methods from the previous challenge 
for this: calc_word_value and max_word_value.

Calculate the optimal word (= max word value) checking all permutations of 
the 7 letters of the draw, cross-checking the DICTIONARY set for valid ones. 
This is a bit more advanced, but allows you to score the player (next).

Show the player what the optimal word and its value is.

Score the player based on the previous steps: player_score / optimal_score.
"""
import itertools
import random
import string
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters(n = NUM_LETTERS, letters = POUCH or string.ascii_uppercase):
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return [random.choice(letters) for i in range(n)]



def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper. """
    word = ""
    while len(word) < 1 or not _validation(word, draw):
        word = input(f"Please enter a word that uses only these letters: {draw}") 
    return word


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    return all(w.upper() in draw.upper() for w in word) and word in DICTIONARY


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    pass


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    return itertools.permutations(draw)


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
