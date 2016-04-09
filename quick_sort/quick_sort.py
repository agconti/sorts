# https://youtu.be/y_G9BkAm6B8?list=PLAB1DA9F452D9466C
# http://visualgo.net/sorting.html
import random


def quick_sort(items):
    if len(items) < 2:
        return items

    pivot = select_pivot(items)
    sort(items, pivot)
    left, right = partition(items, pivot)

    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot] + right


def sort(items, pivot):
    items_length = len(items)
    upper_bound = items_length - 1
    lower_bound = 0
    left = items[lower_bound]
    right = items[upper_bound]

    while True:

        if left == right:
            break

        while items[lower_bound] <= pivot and (items[lower_bound] != pivot):
            lower_bound += 1

        while items[upper_bound] >= pivot and (items[upper_bound] != pivot):
            upper_bound -= 1

        left = items[lower_bound]
        right = items[upper_bound]
        swap(left, lower_bound, right, upper_bound, items)


def swap(left_item, left_index, right_item, right_index, items):
        items[right_index] = left_item
        items[left_index] = right_item


def select_pivot(items):
    return random.choice(items)


def partition(items, pivot):
    pivot_index = items.index(pivot)
    return items[:pivot_index], items[pivot_index + 1:]
