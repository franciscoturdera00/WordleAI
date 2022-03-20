from collections import Counter

from strategies.strategy import Strategy
from strategies.feedback import Feedback
from util.constants import LIST_OF_LETTERS


class SimpleFilterStrategy(Strategy):
    """Filters out words that are no longer possible"""

    def feedback(self, guess, feedback):
        self.possible_answers = self.update_feedback(guess, feedback, self.possible_answers)

    @staticmethod
    def update_feedback(guess, feedback, bank):
        """
        Removes all words from bank that are no longer possible give the feedback
        """
        bank = list(bank)
        letter_found = dict.fromkeys(LIST_OF_LETTERS, 0)
        for i, feed in enumerate(feedback):
            # If letter is correct, eliminate all options
            # where this index is not this letter
            if feed == Feedback.CORRECT:
                letter_found[guess[i]] += 1
                bank[:] = [word for word in bank if word[i] == guess[i]]
            if feed == Feedback.IN_WORD:
                letter_found[guess[i]] += 1

        for ch in letter_found:
            bank[:] = [word for word in bank if letter_found[ch] <= word.count(ch)]

        for i, feed in enumerate(feedback):
            letter = guess[i]
            if feed == Feedback.NOT_IN_WORD:
                # Eliminate all options that contain this letter
                valid_times = letter_found[letter]
                bank[:] = [word for word in bank if word.count(letter) <= valid_times]
            if feed == Feedback.IN_WORD:
                # Since letter is definitely not in this spot,
                # eliminate all options that contains this letter in this spot
                bank[:] = [word for word in bank if word[i] != letter]

        return set(bank)
