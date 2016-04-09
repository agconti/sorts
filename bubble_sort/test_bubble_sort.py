import unittest
from random import random
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        self.unsorted_values = [random() for i in range(20)]

    def test_bubble_sort_returns_an_array(self):
        sorted_values = bubble_sort(self.unsorted_values)
        assert isinstance(sorted_values, list)

    def test_bubble_sort_correctly_sorts(self):
        sorted_values = bubble_sort(self.unsorted_values)
        self.assertEqual(sorted(self.unsorted_values), sorted_values)

if __name__ == '__main__':
    unittest.main()
