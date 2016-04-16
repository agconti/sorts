# https://youtu.be/P00xJgWzz2c?list=PLAB1DA9F452D9466C
# f(n) = c + n x c x n x c x c x c x c x c
# O(n^2), Θ(n^2), Ω(n^2)

def bubble_sort(items):
    number_of_sweeps_left = len(items)

    while number_of_sweeps_left > 0:
        number_of_sweeps_left -= 1

        for index, item in enumerate(items):
            if index == number_of_sweeps_left:
                break

            next_item = items[index + 1]
            if item > next_item:
                items[index] = next_item
                items[index + 1] = item

    return items
