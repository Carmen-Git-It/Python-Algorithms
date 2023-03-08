#
#   Author: Carmen Whitton
#   Github: https://github.com/Carmen-Git-It
#   Date: 2023/03/08
#

import unittest
from binary_search import binary_search


class BinarySearchTestCase(unittest.TestCase):

    def test_empty_list(self):
        values = []

        self.assertEqual(binary_search(values, 5), None)
        self.assertEqual(binary_search(values, None), None)

    def test_list_of_numbers(self):
        values = [-5, 2, 57, 128, 129, 130, 200, 500, 1234, 9999]

        self.assertEqual(binary_search(values, -5), 0)
        self.assertEqual(binary_search(values, -7), None)
        self.assertEqual(binary_search(values, 10245), None)
        self.assertEqual(binary_search(values, 130), 5)
        self.assertEqual(binary_search(values, 9999), 9)


if __name__ == '__main__':
    unittest.main()
