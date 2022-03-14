from collections import Counter

from strategies.smart_guess import SmartGuessStrategy
from util.constants import LIST_OF_LETTERS


class IndexDecisionStrategy(SmartGuessStrategy):
    """
    Strategy works just like SmartGuessStrategy,
    but chooses guess by finding the most common letters in each index of the word instead
    """

    @staticmethod
    def create_weights(words, ordered_letters):
        weights = dict.fromkeys(words, 0)
        for w in words:
            freq = Counter(w)
            for i, letter in enumerate(w):
                weights[w] += ordered_letters[i][letter] / freq[letter]
        return weights

    @staticmethod
    def letter_quantity(bank, word_length):
        letters = [dict.fromkeys(LIST_OF_LETTERS, 0)] * word_length
        for word in bank:
            for i, ch in enumerate(word):
                letters[i][ch] += 1
        return letters

