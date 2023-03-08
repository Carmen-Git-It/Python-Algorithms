#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

import unittest
from bubble_sort import bubble_sort


class BubbleSortTestCase(unittest.TestCase):

    def test_list_of_numbers(self):
        values = [5, 9, 8, 7, 2, 22, 15, 99, 1, -3, 0]
        sorted_values = values.copy()
        sorted_values.sort()

        bubble_sort(values)
        self.assertEqual(values, sorted_values)

    def test_list_of_strings(self):
        values = ["hi", "hello", "goodbye", "almost"]
        sorted_values = values.copy()
        sorted_values.sort()

        bubble_sort(values)
        self.assertEqual(values, sorted_values)


if __name__ == '__main__':
    unittest.main()