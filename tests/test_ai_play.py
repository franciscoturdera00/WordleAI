import os
from pathlib import Path
from unittest import TestCase

from game_logic.ai_play import play_ai
from util.functions import get_official_list, generate_word_from


class Test(TestCase):
    """Integration Tests: Simply tests the strategies don't crash"""

    parent_path = str(Path(os.getcwd()).parent.absolute())
    official_list = get_official_list(parent_path)

    def test_random_strategy(self):
        for i in range(100):
            try:
                lst = self.official_list.copy()
                play_ai("random", lst, generate_word_from(lst), 10)
            except RuntimeError:
                print("RandomStrategy failed in %d run: " % i, RuntimeError)

    def test_simple_filter_strategy(self):
        for i in range(100):
            try:
                lst = self.official_list.copy()
                play_ai("simple_filter", lst, generate_word_from(lst), 10)
            except RuntimeError:
                print("SimpleFilterStrategy failed in %d run: " % i, RuntimeError)

    def test_smart_guess_strategy(self):
        for i in range(100):
            try:
                lst = self.official_list.copy()
                play_ai("smart_guess", lst, generate_word_from(lst), 10)
            except RuntimeError:
                print("SmartGuessStrategy failed in %d run: " % i, RuntimeError)