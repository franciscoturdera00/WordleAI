from unittest import TestCase

from strategies.smart_guess import SmartGuessStrategy
from util.functions import remove_0s


class TestSmartGuessStrategy(TestCase):
    def test_letter_quantity(self):
        bank = ['words', 'loses', 'paint']
        ans = SmartGuessStrategy.letter_quantity(bank, 5)
        self.assertEqual(27, len(ans))
        expected = {'w': 1, 'o': 2, 'r': 1, 'd': 1, 's': 3,
                    'l': 1, 'e': 1, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 't': 1}
        self.assertEqual(expected, remove_0s(ans))
