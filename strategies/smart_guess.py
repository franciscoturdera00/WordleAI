import random
from collections import Counter

from strategies.simple_filter import SimpleFilterStrategy
from util.constants import LIST_OF_LETTERS
from util.functions import quantity_ordered_list


def find_best_guess(ordered_letters, words):
    weights = dict.fromkeys(words, 0)
    for letter in ordered_letters:
        for w in words:
            if letter[0] in w:
                freq = Counter(letter[0])
                repeated = len(w) - len(freq)
                weights[w] += letter[1] / repeated
    return weights


def letter_quantity(bank):
    letters = dict.fromkeys(LIST_OF_LETTERS, 0)
    for word in bank:
        for ch in word:
            letters[ch] += 1
    return letters


class SmartGuessStrategy(SimpleFilterStrategy):
    """
    Strategy works just like SimpleFilterStrategy,
    but chooses guess by finding the most common letters in word bank
    and best fitting word to gather as much info as possible
    """

    def guess(self):
        ordered_letters = quantity_ordered_list(letter_quantity(self.possible_answers))
        weights = find_best_guess(ordered_letters, self.possible_answers)
        ordered_list = quantity_ordered_list(weights)
        standard = ordered_list[0][1]
        filtered = list(filter(lambda x: x[1] == standard, ordered_list))
        guess = random.sample(filtered, 1)[0][0]
        return guess
