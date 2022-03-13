from unittest import TestCase

from game_logic.ai_play import play_ai
from util.functions import get_official_list


class Test(TestCase):
    """Integration Tests: Simply tests the strategies don't crash"""

    def test_random_strategy(self):

        for i in range(100):
            try:
                play_ai("random", get_official_list(), "words", 10)
            except RuntimeError:
                print("RandomStrategy failed in %d run: " % i, RuntimeError)

    def test_basic_filter_strategy(self):
        for i in range(100):
            try:
                play_ai("simple_filter", get_official_list(), "banks", 10)
            except RuntimeError:
                print("SimpleFilterStrategy failed in %d run: " % i, RuntimeError)
