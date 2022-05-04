import os
from pathlib import Path
from unittest import TestCase

from game_logic.ai_play import play_game
from strategies.index_decision import IndexDecisionStrategy
from strategies.markov import MarkovStrategy
from strategies.outside_the_box import ThinkOutsideTheBoxStrategy
from strategies.random_strategy import RandomStrategy
from strategies.simple_filter import SimpleFilterStrategy
from strategies.smart_guess import SmartGuessStrategy
from util.functions import (
    get_official_list,
    generate_word_from,
    get_official_guess_list,
)


LOOP = 50


class Test(TestCase):
    """Integration Tests: Simply tests the strategies don't crash"""

    current_file = os.path.dirname(__file__)
    grand_parent_path = str(Path(current_file).absolute().parent.absolute().parent.absolute())
    official_list = get_official_list(grand_parent_path)

    def test_random_strategy(self):
        for _ in range(LOOP):
            lst = self.official_list.copy()
            strat = RandomStrategy(lst.copy(), set(), 5, 6)
            play_game(strat, lst, set(), generate_word_from(lst), 10)

    def test_simple_filter_strategy(self):
        for _ in range(LOOP):
            lst = self.official_list.copy()
            strat = SimpleFilterStrategy(lst.copy(), set(), 5, 6)
            play_game(strat, lst, set(), generate_word_from(lst), 10)

    def test_smart_guess_strategy(self):
        for _ in range(LOOP):
            lst = self.official_list.copy()
            strat = SmartGuessStrategy(lst.copy(), set(), 5, 6)
            play_game(strat, lst, set(), generate_word_from(lst), 10)

    def test_index_decision_strategy(self):
        for _ in range(LOOP):
            lst = self.official_list.copy()
            strat = IndexDecisionStrategy(lst.copy(), set(), 5, 6)
            play_game(strat, lst, set(), generate_word_from(lst), 10)

    def test_outside_the_box_strategy(self):
        for _ in range(LOOP):
            lst = self.official_list.copy()
            secret = get_official_guess_list(self.grand_parent_path)
            strat = ThinkOutsideTheBoxStrategy(lst.copy(), secret.copy(), 5, 6)
            play_game(strat, lst, secret, generate_word_from(lst), 10)

    def test_markov_strategy(self):
        for _ in range(LOOP):
            lst = self.official_list.copy()
            strat = MarkovStrategy(lst.copy(), set(), 5, 6)
            play_game(strat, lst, set(), generate_word_from(lst), 10)
