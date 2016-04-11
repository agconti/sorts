import unittest
from random import random
from heap_sort import heap_sort


class TestHeapSort(unittest.TestCase):

    def setUp(self):
        self.unsorted_values = [random() for i in range(20)]

    def test_heap_sort_returns_an_array(self):
        sorted_values = heap_sort(self.unsorted_values)
        assert isinstance(sorted_values, list)

    def test_heap_sort_does_not_mutate_input(self):
        values = list(self.unsorted_values)
        sorted_values = heap_sort(self.unsorted_values)
        self.assertEqual(self.unsorted_values, values)

    def test_heap_sort_correctly_sorts(self):
        sorted_values = heap_sort(self.unsorted_values)
        self.assertEqual(sorted(self.unsorted_values), sorted_values)

if __name__ == '__main__':
    unittest.main()
