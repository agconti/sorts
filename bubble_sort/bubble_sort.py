#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://youtu.be/P00xJgWzz2c?list=PLAB1DA9F452D9466C
# f(n) = c + n x c x n x c x c x c x c x c
# O(n^2), Θ(n^2), Ω(n^2)


def bubble_sort(items):
    swapped = True
    sweeps_left = len(items)

    while sweeps_left > 0 and swapped:
        swapped = False
        sweeps_left -= 1

        for index in range(sweeps_left):

            item = items[index]
            next_item = items[index + 1]
            if item > next_item:
                items[index] = next_item
                items[index + 1] = item
                swapped = True

    return items
