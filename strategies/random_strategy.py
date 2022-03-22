from strategies.strategy import Strategy
from util.functions import generate_word_from


class RandomStrategy(Strategy):
    """Choose randomly from the sample space"""

    def guess(self):
        guess = generate_word_from(self.possible_answers)
        self.possible_answers.remove(guess)
        return guess
