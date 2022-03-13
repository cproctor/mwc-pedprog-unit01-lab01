# test_list_functions
# by Chris Proctor
#
# This module imports `list_functions` and tests its functions
# to see if they work properly.
#
# Note: This module uses concepts you haven't learned yet; you 
# are not expected to understand it. Of course, if you're interested, 
# just ask!

from unittest import TestCase, main
from list_functions import (
    square_list,
    capitalize_list,
    pluralize_list,
    reverse_list,
)

class TestSquareList(TestCase):
    def test_squares_numbers(self):
        odd_numbers = [1, 3, 5, 7, 9]
        expected = [num ** 2 for num in odd_numbers]
        observed = square_list(odd_numbers)
        self.assertTrue(isinstance(observed, list))
        self.assertEqual(len(expected), len(observed))
        for exp, obs in zip(expected, observed):
            self.assertEqual(exp, obs)

class TestCapitalizeList(TestCase):
    def test_capitalizes_words(self):
        animals = ["emu", "giraffe", "panda", "mouse"]
        expected = [word.upper() for word in animals]
        observed = capitalize_list(animals)
        self.assertTrue(isinstance(observed, list))
        self.assertEqual(len(expected), len(observed))
        for exp, obs in zip(expected, observed):
            self.assertEqual(exp, obs)

class TestPluralizeList(TestCase):
    def test_pluralizes(self):
        animals = ["emu", "giraffe", "panda", "mouse"]
        expected = [word + 's' for word in animals]
        observed = pluralize_list(animals)
        self.assertTrue(isinstance(observed, list))
        self.assertEqual(len(expected), len(observed))
        for exp, obs in zip(expected, observed):
            self.assertEqual(exp, obs)

class TestReverseList(TestCase):
    def test_reverses(self):
        odd_numbers = [1, 3, 5, 7, 9]
        expected = list(reversed(odd_numbers))
        observed = reverse_list(odd_numbers)
        self.assertTrue(isinstance(observed, list))
        self.assertEqual(len(expected), len(observed))
        for exp, obs in zip(expected, observed):
            self.assertEqual(exp, obs)

if __name__ == '__main__':
    main()
