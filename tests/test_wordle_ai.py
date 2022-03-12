from unittest import TestCase

from strategies.feedback import Feedback
from wordle_ai import analyze_guess


class Test(TestCase):
    def test_analyze_guess(self):
        perfect = [Feedback.CORRECT] * 5
        self.assertEqual(perfect, analyze_guess("words", "words"))

        all_bad = [Feedback.NOT_IN_WORD] * 8
        self.assertEqual(all_bad, analyze_guess("lkostasc", "pireqwmn"))

        # If failing, probably checking multiple letters wrong
        hello_expected = [Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD,
                          Feedback.CORRECT, Feedback.IN_WORD]
        self.assertEqual(hello_expected, analyze_guess("hello", "world"))
