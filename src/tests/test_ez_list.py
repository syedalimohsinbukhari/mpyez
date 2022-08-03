import unittest

import src.ezPy.ez_list as ez_list
from src.ezPy.utilities.ez_list import errors


class Test(unittest.TestCase):
    def test_numeric_list_to_string(self):
        self.assertEqual(ez_list.numeric_list_to_string([1, 2, 3]), ['1', '2', '3'])

    def test_string_list_to_numeric(self):
        self.assertEqual(ez_list.string_list_to_numeric(['1', '2', '3']), [1, 2, 3])

        with self.assertRaises(errors.AlphabetFound):
            ez_list.string_list_to_numeric(['A'])

    def test_nested_list_to_list(self):
        self.assertEqual(ez_list.nested_list_to_list([[1, 2, 3, 4], [5, 6, 7, 8]]),
                         [1, 2, 3, 4, 5, 6, 7, 8])

    def test_list_to_nested_list(self):
        self.assertEqual(ez_list.list_to_nested_list([1, 2, 3, 4, 5, 6], 2),
                         [[1, 2], [3, 4], [5, 6]])
        self.assertEqual(ez_list.list_to_nested_list([1, 2, 3, 4, 5, 6], 3),
                         [[1, 2, 3], [4, 5, 6]])

    def test_join_lists(self):
        self.assertEqual(ez_list.join_lists([[1, 2, 3], [5, 6, 4]]),
                         [1, 2, 3, 5, 6, 4])

        self.assertEqual(ez_list.join_lists([[1, 2, 3], [5, 6, 4]], sort=True),
                         [1, 2, 3, 4, 5, 6])

        self.assertEqual(ez_list.join_lists([[[1, 2], 3], [5, 6, 4]], sort=True),
                         [(1, 2), 3, 4, 5, 6])

        self.assertEqual(ez_list.join_lists([[[1, 2], 3], [[1, 2], 5, 6, 4]], get_unique=True,
                                            sort=True), [(1, 2), 3, 4, 5, 6])

        self.assertEqual(ez_list.join_lists([[[1, 2], 3], [[1, 2], 5, 6, 4]], get_unique=True,
                                            sort=True, tuples_as_lists=True), [[1, 2], 3, 4, 5, 6])

    def test_is_contained(self):
        a, b = [1, 2, 3], [1, 2, 3, 4]

        self.assertEqual(ez_list.is_contained(a, b), True)
        self.assertEqual(ez_list.is_contained(b, a), False)

    def test_Replace__single_index(self):
        inp_, ind_, wth_ = [1, 2, 3, 4, 5], 0, 10

        rep = ez_list.Replace(inp_, ind_, wth_)
        self.assertEqual(rep.at_index(), [10, 2, 3, 4, 5])

    def test_Replace__multi_index(self):
        inp_, ind_, wth_ = [1, 2, 3, 4, 5], [0, 2, 3], [10, 10, 10]

        rep = ez_list.Replace(inp_, ind_, wth_)
        self.assertEqual(rep.at_index(), [10, 2, 10, 10, 5])

    def test_Replace__single_index__multiple_values(self):
        inp_, ind_, wth_ = [1, 2, 3, 4, 5], 0, [10, 10, 10]

        with self.assertRaises(errors.UnequalElements):
            ez_list.Replace(inp_, ind_, wth_).at_index()

    def test_Replace__multi_value(self):
        inp_, val_, wth_ = [1, 2, 3, 4, 5], [2, 3], [10, 12]

        rep = ez_list.Replace(inp_, val_, wth_, 'value')
        self.assertEqual(rep.at_value(), [1, 10, 12, 4, 5])
