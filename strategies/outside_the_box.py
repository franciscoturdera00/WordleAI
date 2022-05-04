from strategies.index_decision import IndexDecisionStrategy
from util.functions import quantity_ordered_list, flip_weighted_coin, generate_word_from


class ThinkOutsideTheBoxStrategy(IndexDecisionStrategy):
    """
    Works just like IndexDecisionStrategy but uses explore/exploit
    approach regarding the usage of an auxiliary word list
    """

    def __init__(self, word_bank, secret_bank, length_of_word, attempts):
        super().__init__(word_bank, secret_bank, length_of_word, attempts)
        self.initial_word_bank_length = len(self.possible_answers)
        self.attempts_left = attempts
        self.CHANCE_CONSTANT = 1.0

    def guess(self):
        ordered_letters = self.letter_quantity(self.possible_answers, self.length_of_word)
        weights_bank = self.create_weights(ordered_letters, self.possible_answers)
        ordered_list = quantity_ordered_list(weights_bank, "regular")
        probability = (self.attempts_left / self.CHANCE_CONSTANT) / self.total_attempts * 1.0
        if flip_weighted_coin(probability):
            weights_secret = self.create_weights(ordered_letters, self.secret_bank)
            ordered_list += quantity_ordered_list(weights_secret, "secret")
            ordered_list.sort(key=lambda x: x[1], reverse=True)
        standard = ordered_list[0][1]
        filtered = list(filter(lambda x: x[1] == standard, ordered_list))
        # If words from the word bank are tied in top weight, use those
        try_from_bank = list(filter(lambda x: x[2] == "regular", filtered))
        optimal = filtered
        if try_from_bank:
            optimal = try_from_bank
        guess = generate_word_from(optimal)[0]
        self.attempts_left -= 1
        self.possible_answers.discard(guess)
        self.secret_bank.discard(guess)
        return guess
