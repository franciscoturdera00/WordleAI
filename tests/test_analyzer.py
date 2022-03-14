from unittest import TestCase

from game_logic.analyzer import analyze_guess
from strategies.feedback import Feedback


class Test(TestCase):
    def test_analyze_guess_basic(self):
        perfect = [Feedback.CORRECT] * 5
        self.assertEqual(perfect, analyze_guess("words", "words"))

        all_bad = [Feedback.NOT_IN_WORD] * 8
        self.assertEqual(all_bad, analyze_guess("lkostasc", "pireqwmn"))

    def test_analyze_guess_dups(self):
        """If failing, probably checking multiple letters wrong"""
        hello_expected = [Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD,
                          Feedback.CORRECT, Feedback.IN_WORD]
        self.assertEqual(hello_expected, analyze_guess("hello", "world"))

        dared_expected = [Feedback.IN_WORD, Feedback.NOT_IN_WORD, Feedback.CORRECT,
                          Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD]
        self.assertEqual(dared_expected, analyze_guess("dared", "words"))

        multiple_repeat = [Feedback.CORRECT, Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD,
                           Feedback.CORRECT, Feedback.NOT_IN_WORD]
        self.assertEqual(multiple_repeat, analyze_guess("props", "ppppp"))

        only_one_in = [Feedback.IN_WORD, Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD,
                       Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD]
        self.assertEqual(only_one_in, analyze_guess("pppkpp", "respta"))

        two_in = [Feedback.NOT_IN_WORD, Feedback.IN_WORD, Feedback.IN_WORD,
                  Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD, Feedback.NOT_IN_WORD]
        self.assertEqual(two_in, analyze_guess("kppkpp", "pespta"))
