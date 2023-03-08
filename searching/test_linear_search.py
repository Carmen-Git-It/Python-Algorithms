#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

import unittest
from linear_search import linear_search


class LinearSearchTestCase(unittest.TestCase):

    def test_empty_list(self):
        values = []

        self.assertEqual(linear_search(values, 5), None)
        self.assertEqual(linear_search(values, None), None)

    def test_list_of_numbers(self):
        values = [5, 9, 8, 7, 2, 22, 15, 99, 1, -3, 0]

        self.assertEqual(linear_search(values, 5), 0)
        self.assertEqual(linear_search(values, -5), None)
        self.assertEqual(linear_search(values, 0), 10)
        self.assertEqual(linear_search(values, 22), 5)

    def test_list_of_strings(self):
        values = ["hi", "hello", "goodbye", "almost"]

        self.assertEqual(linear_search(values, "nope"), None)
        self.assertEqual(linear_search(values, "hi"), 0)
        self.assertEqual(linear_search(values, "goodbye"), 2)
        self.assertEqual(linear_search(values, "almost"), 3)


if __name__ == '__main__':
    unittest.main()
