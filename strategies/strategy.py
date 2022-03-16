import random

from util.functions import generate_word_from


class Strategy:
    """Parent Class for all Strategies"""

    def __init__(self, word_bank, secret_bank, length_of_word, attempts):
        self.possible_answers = word_bank
        self.secret_bank = secret_bank - word_bank
        self.length_of_word = length_of_word
        self.total_attempts = attempts

    def guess(self):
        """Returns the guess that this Strategy takes based on its current state"""
        """Default Strategy: Choose randomly from the sample space"""
        guess = generate_word_from(self.possible_answers)
        self.possible_answers.remove(guess)
        self.secret_bank.discard(guess)
        return guess

    def feedback(self, guess, feedback):
        """Updates Information given new clues"""
