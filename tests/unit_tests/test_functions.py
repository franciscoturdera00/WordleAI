from unittest import TestCase

from util.functions import flatten, generate_word_from, quantity_ordered_list

class TestFunctions(TestCase):

    def test_generate_word_from(self):
        word_list = ["hello", "world", "fakes", "least"]
        word_list_size = len(word_list)
        word = generate_word_from(word_list)
        self.assertTrue(word in word_list)
        self.assertAlmostEqual(len(word_list), word_list_size)

    def test_quantity_ordered_list(self):
        w_map = {"hello": 5, "paint": 2, "barks": 4}
        ordered = [("hello", 5), ("barks", 4), ("paint", 2)]
        w_map_ordered = quantity_ordered_list(w_map)
        self.assertEqual(w_map_ordered, ordered)


    def test_flatten(self):
        unflat = [["hi", "pants"], ["legs"]]
        flat = ["hi", "pants", "legs"]
        self.assertEqual(flatten(unflat), flat)
