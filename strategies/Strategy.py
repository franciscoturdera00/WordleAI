import random
from strategies.space import Space


class Strategy:

    def __init__(self, word_bank, length_of_word):
        self.possible_answers = word_bank
        solution = {}
        for i in range(length_of_word):
            solution[i] = Space()

    def guess(self):
        """Returns the guess that this Strategy takes based on its current state"""
        """Default Strategy: Choose randomly from the sample space"""
        guess = random.sample(self.possible_answers, 1)[0]
        self.possible_answers.remove(guess)
        return guess

    def feedback(self, guess, feedback):
        """Updates Information given new clues"""
        pass
