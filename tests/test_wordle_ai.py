import os
from unittest import TestCase
from pathlib import Path

from strategies.feedback import Feedback
from wordle_ai import analyze_guess, play


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

    """Integration Tests: Simply tests the strategies don't crash"""
    @staticmethod
    def getParentPath():
        path = Path(os.getcwd())
        return str(path.parent.absolute())

    def get_official_list(self):
        with open(self.getParentPath() + "/word_banks/wordle_official_list.txt") as f:
            official_list = [x.replace("\n", "") for x in f.readlines()]
        return set(official_list)

    def test_random_strategy(self):

        for i in range(100):
            try:
                play("random", self.get_official_list(), "words", 10)
            except RuntimeError:
                print("RandomStrategy failed in %d run: " % i, RuntimeError)

    def test_basic_filter_strategy(self):
        for i in range(100):
            try:
                play("simple_filter", self.get_official_list(), "banks", 10)
            except RuntimeError:
                print("SimpleFilterStrategy failed in %d run: " % i, RuntimeError)
