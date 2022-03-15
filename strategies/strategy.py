import random


class Strategy:
    """Parent Class for all Strategies"""

    def __init__(self, word_bank, length_of_word):
        self.word_bank = word_bank
        self.possible_answers = word_bank.copy()
        self.length_of_word = length_of_word

    def guess(self):
        """Returns the guess that this Strategy takes based on its current state"""
        """Default Strategy: Choose randomly from the sample space"""
        guess = random.choice(list(self.possible_answers))
        self.possible_answers.remove(guess)
        return guess, [self.word_bank]

    def feedback(self, guess, feedback):
        """Updates Information given new clues"""
        self.word_bank.remove(guess)
