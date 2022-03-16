from collections import Counter

from strategies.strategy import Strategy
from strategies.feedback import Feedback
from util.constants import LIST_OF_LETTERS


class SimpleFilterStrategy(Strategy):
    """Filters out words that are no longer possible"""

    def feedback(self, guess, feedback):
        self.update_feedback(guess, feedback, self.possible_answers)

    @staticmethod
    def update_feedback(guess, feedback, bank):
        letter_found = dict.fromkeys(LIST_OF_LETTERS, 0)
        for i, feed in enumerate(feedback):
            # If letter is correct, eliminate all options
            # where this index is not this letter
            if feed == Feedback.CORRECT:
                letter_found[guess[i]] += 1
                static_words = bank.copy()
                for word in static_words:
                    if word[i] != guess[i]:
                        bank.discard(word)
            if feed == Feedback.IN_WORD:
                letter_found[guess[i]] += 1

        # Eliminate all options that have less repeating letters than found
        static_words = bank.copy()
        for word in static_words:
            freq = Counter(word)
            for f in freq:
                if letter_found[f] > freq[f]:
                    bank.discard(word)

        for i, feed in enumerate(feedback):
            letter = guess[i]
            if feed == Feedback.NOT_IN_WORD:
                # Eliminate all options that contain this letter
                valid_times = letter_found[letter]
                static_words = bank.copy()
                for word in static_words:
                    if word.count(letter) > valid_times:
                        bank.discard(word)
            if feed == Feedback.IN_WORD:
                # Since letter is definitely not in this spot,
                # eliminate all options that contains this letter in this spot
                static_words = bank.copy()
                for word in static_words:
                    if word[i] == letter:
                        bank.discard(word)

