import os
from pathlib import Path
from unittest import TestCase

from game_logic.ai_play import play_ai
from util.functions import (
    get_official_list,
    generate_word_from,
    get_official_guess_list,
)


class Test(TestCase):
    """Integration Tests: Simply tests the strategies don't crash"""

    current_file = os.path.dirname(__file__)
    grand_parent_path = str(
        Path(current_file).absolute().parent.absolute().parent.absolute()
    )
    official_list = get_official_list(grand_parent_path)

    def test_random_strategy(self):
        for i in range(100):
            lst = self.official_list.copy()
            play_ai("random", lst, set(), generate_word_from(lst), 10)

    def test_simple_filter_strategy(self):
        for i in range(100):
            lst = self.official_list.copy()
            play_ai("simple_filter", lst, set(), generate_word_from(lst), 10)

    def test_smart_guess_strategy(self):
        for i in range(100):
            lst = self.official_list.copy()
            play_ai("smart_guess", lst, set(), generate_word_from(lst), 10)

    def test_index_decision_strategy(self):
        for i in range(100):
            lst = self.official_list.copy()
            play_ai("index_decision", lst, set(), generate_word_from(lst), 10)

    def test_outside_the_box_strategy(self):
        for i in range(100):
            lst = self.official_list.copy()
            secret = get_official_guess_list(self.grand_parent_path)
            play_ai("outside_the_box", lst, secret, generate_word_from(lst), 10)

    def test_markov_strategy(self):
        for i in range(100):
            lst = self.official_list.copy()
            play_ai("markov", lst, set(), generate_word_from(lst), 10)
