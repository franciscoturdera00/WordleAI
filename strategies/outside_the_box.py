import random

from strategies.index_decision import IndexDecisionStrategy
from util.functions import quantity_ordered_list, flip_weighted_coin, generate_word_from


class ThinkOutsideTheBoxStrategy(IndexDecisionStrategy):

    def __init__(self, word_bank, secret_bank, length_of_word, attempts):
        super().__init__(word_bank, secret_bank, length_of_word, attempts)
        self.initial_word_bank_length = len(self.possible_answers)
        self.attempts_left = attempts
        self.CHANCE_CONSTANT = 1.0

    def guess(self):
        ordered_letters = self.letter_quantity(self.possible_answers, self.length_of_word)
        weights_bank = self.create_weights(ordered_letters, self.possible_answers)
        ordered_list = quantity_ordered_list(weights_bank, "regular")
        probability = 1 - ((self.total_attempts - (self.attempts_left / self.CHANCE_CONSTANT))
                           / (self.total_attempts * 1.0))
        if flip_weighted_coin(probability) and len(self.possible_answers) > 1:
            weights_secret = self.create_weights(ordered_letters, self.secret_bank)
            ordered_list += quantity_ordered_list(weights_secret, "secret")
            ordered_list.sort(key=lambda x: x[1], reverse=True)
        standard = ordered_list[0][1]
        filtered = list(filter(lambda x: x[1] == standard, ordered_list))
        guess = generate_word_from(filtered)[0]
        self.attempts_left -= 1
        self.possible_answers.discard(guess)
        self.secret_bank.discard(guess)
        return guess

    def feedback(self, guess, feedback):
        super().feedback(guess, feedback)
        self.update_feedback(guess, feedback, self.secret_bank)
