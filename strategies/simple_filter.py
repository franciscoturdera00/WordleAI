from strategies.Strategy import Strategy
from strategies.feedback import Feedback
from util.constants import LIST_OF_LETTERS


class SimpleFilterStrategy(Strategy):
    """Filters out words that are no longer possible"""

    def feedback(self, guess, feedback):
        letter_found = dict.fromkeys(LIST_OF_LETTERS, 0)
        for i, feed in enumerate(feedback):
            if feed == Feedback.CORRECT:
                letter_found[guess[i]] += 1
                static_words = self.possible_answers.copy()
                for word in static_words:
                    if word[i] != guess[i]:
                        self.possible_answers.remove(word)
            if feed == Feedback.IN_WORD:
                letter_found[guess[i]] += 1

        for ch in letter_found:
            static_words = self.possible_answers.copy()
            for word in static_words:
                if letter_found[ch] > word.count(ch):
                    self.possible_answers.remove(word)

        for i, feed in enumerate(feedback):
            if feed == Feedback.NOT_IN_WORD:
                letter = guess[i]
                valid_times = letter_found[letter]
                static_words = self.possible_answers.copy()
                for word in static_words:
                    if word.count(letter) > valid_times:
                        self.possible_answers.remove(word)
        print(len(self.possible_answers))

