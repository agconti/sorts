import unittest
from random import random
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.unsorted_values = [random() for i in range(20)]

    def test_insertion_sort_returns_an_array(self):
        sorted_vales = insertion_sort(self.unsorted_values)
        assert isinstance(sorted_vales, list)

    def test_insertion_sort_does_not_mutate_input(self):
        values = list(self.unsorted_values)
        sorted_vales = insertion_sort(self.unsorted_values)
        self.assertEqual(self.unsorted_values, values)

    def test_insertion_sort_correctly_sorts(self):
        sorted_vales = insertion_sort(self.unsorted_values)
        self.assertEqual(sorted(self.unsorted_values), sorted_vales)

if __name__ == '__main__':
    unittest.main()
