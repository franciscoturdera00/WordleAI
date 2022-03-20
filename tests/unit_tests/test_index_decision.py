from unittest import TestCase

from strategies.index_decision import IndexDecisionStrategy
from util.functions import remove_0s


class TestIndexDecisionStrategy(TestCase):
    def test_letter_quantity(self):
        bank = ['words', 'loses', 'paint']
        ans = IndexDecisionStrategy.letter_quantity(bank, 5)
        self.assertEqual(5, len(ans))
        for a in ans:
            self.assertEqual(27, len(a))
        expected = [{'w': 1, 'l': 1, 'p': 1},
                    {'o': 2, 'a': 1},
                    {'r': 1, 's': 1, 'i': 1},
                    {'d': 1, 'e': 1, 'n': 1},
                    {'s': 2, 't': 1}]
        clean_ans = [remove_0s(a) for a in ans]
        self.assertEqual(expected, clean_ans)
