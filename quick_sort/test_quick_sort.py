import unittest
from random import random
from quick_sort import quick_sort, select_pivot, swap, partition, sort


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        self.unsorted_values = [random() for i in range(5)]

    def test_select_pivot_return_an_item_from_array(self):
        assert select_pivot(self.unsorted_values) in self.unsorted_values

    def test_swap_switched_items(self):
        items = [0, 1]
        swap(items[0], 0, items[1], 1, items)
        self.assertEqual(items, [1, 0])

    def test_partition_returns_two_split_arrays(self):
        values = range(10)
        pivot = 5
        a, b = partition(values, pivot)

        assert isinstance(a, list)
        assert isinstance(b, list)

    def test_partition_does_not_contain_pivot(self):
        values = range(10)
        pivot = 5
        a, b = partition(values, pivot)

        assert pivot not in a
        assert pivot not in b

    def test_sort_partially_sorts_items_compared_to_pivot(self):
        values = range(10)
        pivot = 5

        sort(values, pivot)
        smaller = values[:pivot]
        larger = values[pivot + 1:]

        for item in smaller:
            assert item < pivot

        for item in larger:
            assert item > pivot

    def test_quick_sort_returns_an_array(self):
        sorted_values = quick_sort(self.unsorted_values)
        assert isinstance(sorted_values, list)

    def test_quick_sort_correctly_sorts(self):
        sorted_values = quick_sort(self.unsorted_values)
        self.assertEqual(sorted(self.unsorted_values), sorted_values)

if __name__ == '__main__':
    unittest.main()
