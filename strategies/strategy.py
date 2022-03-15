import random


class Strategy:
    """Parent Class for all Strategies"""

    def __init__(self, word_bank, secret_bank, length_of_word):
        self.possible_answers = word_bank
        self.secret_bank = secret_bank
        self.length_of_word = length_of_word

    def guess(self):
        """Returns the guess that this Strategy takes based on its current state"""
        """Default Strategy: Choose randomly from the sample space"""
        guess = random.choice(list(self.possible_answers))
        self.possible_answers.remove(guess)
        self.secret_bank.discard(guess)
        return guess

    def feedback(self, guess, feedback):
        """Updates Information given new clues"""
