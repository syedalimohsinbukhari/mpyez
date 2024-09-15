"""Created on Jun 12 13:49:07 2022"""

import unittest

from ..mpyez import ezList
from ..mpyez.backend import uList
from ..mpyez.backend.eList import AlphabetFound, UnequalElements


class Test(unittest.TestCase):
    def test_numeric_list_to_string(self):
        self.assertEqual(uList.numeric_list_to_string([1, 2, 3]), ['1', '2', '3'])

    def test_string_list_to_numeric(self):
        self.assertEqual(ezList.string_list_to_numeric(['1', '2', '3']), [1, 2, 3])

        with self.assertRaises(AlphabetFound):
            ezList.string_list_to_numeric(['A'])

    def test_nested_list_to_list(self):
        self.assertEqual(ezList.nested_list_to_list([[1, 2, 3, 4], [5, 6, 7, 8]]),
                         [1, 2, 3, 4, 5, 6, 7, 8])

    def test_list_to_nested_list(self):
        self.assertEqual(ezList.list_to_nested_list([1, 2, 3, 4, 5, 6], 2),
                         [[1, 2], [3, 4], [5, 6]])
        self.assertEqual(ezList.list_to_nested_list([1, 2, 3, 4, 5, 6], 3),
                         [[1, 2, 3], [4, 5, 6]])

    def test_join_lists(self):
        self.assertEqual(ezList.join_lists([[1, 2, 3], [5, 6, 4]]),
                         [1, 2, 3, 5, 6, 4])

        self.assertEqual(ezList.join_lists([[1, 2, 3], [5, 6, 4]], sort=True),
                         [1, 2, 3, 4, 5, 6])

    def test_is_contained(self):
        a, b = [1, 2, 3], [1, 2, 3, 4]

        self.assertEqual(ezList.is_contained(a, b), True)
        self.assertEqual(ezList.is_contained(b, a), False)

    def test_Replace__single_index(self):
        inp_, ind_, wth_ = [1, 2, 3, 4, 5], 0, 10

        self.assertEqual(ezList.replace_at_index(inp_, ind_, wth_), [10, 2, 3, 4, 5])

    def test_Replace__multi_index(self):
        inp_, ind_, wth_ = [1, 2, 3, 4, 5], [0, 2, 3], [10, 10, 10]

        self.assertEqual(ezList.replace_at_index(inp_, ind_, wth_), [10, 2, 10, 10, 5])

    def test_Replace__single_index__multiple_values(self):
        inp_, ind_, wth_ = [1, 2, 3, 4, 5], 0, [10, 10, 10]

        with self.assertRaises(UnequalElements):
            ezList.replace_at_index(inp_, ind_, wth_)

    def test_Replace__multi_value(self):
        inp_, val_, wth_ = [1, 2, 3, 4, 5], [2, 3], [10, 12]

        self.assertEqual(ezList.replace_with_value(inp_, val_, wth_), [1, 10, 12, 4, 5])
