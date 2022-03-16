import random
from collections import Counter

from strategies.simple_filter import SimpleFilterStrategy
from util.constants import LIST_OF_LETTERS
from util.functions import quantity_ordered_list


class SmartGuessStrategy(SimpleFilterStrategy):
    """
    Strategy works just like SimpleFilterStrategy,
    but chooses guess by finding the most common letters in word bank
    and best fitting word to gather as much info as possible
    """

    def guess(self):
        ordered_letters = self.letter_quantity(self.possible_answers, self.length_of_word)
        weights = self.create_weights(ordered_letters, self.possible_answers)
        ordered_list = quantity_ordered_list(weights)
        standard = ordered_list[0][1]
        filtered = list(filter(lambda x: x[1] == standard, ordered_list))
        guess = random.choice(filtered)[0]
        return guess

    @staticmethod
    def create_weights(ordered_letters, words):
        weights = dict.fromkeys(words, 0)
        for w in words:
            freq = Counter(w)
            for ch in freq:
                weights[w] += ordered_letters[ch] / freq[ch]
        return weights

    @staticmethod
    def letter_quantity(bank, word_length):
        letters = dict.fromkeys(LIST_OF_LETTERS, 0)
        for word in bank:
            for ch in word:
                letters[ch] += 1
        return letters
