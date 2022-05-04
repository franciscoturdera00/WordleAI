from strategies.feedback import Feedback
from strategies.index_decision import IndexDecisionStrategy
from util.functions import get_product, generate_word_from


class MarkovStrategy(IndexDecisionStrategy):
    """
    Uses Index Decision for first guess and then takes advantage of the
    Markov Chain Modelto choose a guess which will yield to the highest
    probability of getting the right answer in the following guess
    """

    def __init__(self, word_bank, secret_bank, length_of_word, attempts):
        super().__init__(word_bank, secret_bank, length_of_word, attempts)
        self.prod = get_product(
            length_of_word, Feedback.NOT_IN_WORD, Feedback.IN_WORD, Feedback.CORRECT
        )
        self.first_guess = True

    def guess(self):
        if self.first_guess:
            self.first_guess = False
            return super().guess()
        weights = [
            (word, self.return_probability_of_correct_in(word))
            for word in self.possible_answers
        ]
        weights.sort(key=lambda x: x[1], reverse=True)
        standard = weights[0][1]
        filtered = list(filter(lambda x: x[1] == standard, weights))
        chosen = generate_word_from(filtered)
        return chosen[0]

    def return_probability_of_correct_in(self, guess):
        weighted_prob = 0
        for i, p in enumerate(self.prod):
            all_green = all(map(lambda x: x == Feedback.CORRECT, p))
            if all_green:
                weighted_prob = (i * weighted_prob + 1) / (i + 1)
                continue
            new_bank_size = len(
                self.update_feedback(guess, p, self.possible_answers.copy())
            )
            if new_bank_size == 0:
                continue
            probability = 1.0 / new_bank_size
            weighted_prob = (i * weighted_prob + probability) / (i + 1)
        return weighted_prob
