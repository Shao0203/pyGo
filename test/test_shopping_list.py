import unittest
from module.shopping_list import Sentence, ShoppingList


class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence = Sentence('hello world!')

    def test_letter_count(self):
        self.assertEqual(self.sentence.letter_count(), 12)

    def test_word_count(self):
        self.assertEqual(self.sentence.word_count(), 2)

    def test_upper_case(self):
        self.assertEqual(self.sentence.uppertize(), 'HELLO WORLD!')


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList(
            {'apple': 5, 'pear': 15, 'orange': 7})

    def test_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 27)
