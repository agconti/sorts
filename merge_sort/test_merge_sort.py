import unittest
from random import random
from merge_sort import merge_sort, merge


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        self.unsorted_values = [random() for i in range(5)]

    def test_merge_returns_sorted_array(self):
        list_a = [i for i in range(5)]
        list_b = [i for i in range(5, 11)]
        controll_list = list(list_a + list_b)

        merged_list = merge(list_a, list_b)
        self.assertEqual(merged_list, controll_list)

    def test_merge_sort_returns_an_array(self):
        sorted_values = merge_sort(self.unsorted_values)
        assert isinstance(sorted_values, list)

    def test_merge_sort_does_not_mutate_input(self):
        values = list(self.unsorted_values)
        sorted_values = merge_sort(self.unsorted_values)
        self.assertEqual(self.unsorted_values, values)

    def test_merge_sort_correctly_sorts(self):
        sorted_values = merge_sort(self.unsorted_values)
        self.assertEqual(sorted(self.unsorted_values), sorted_values)

if __name__ == '__main__':
    unittest.main()
