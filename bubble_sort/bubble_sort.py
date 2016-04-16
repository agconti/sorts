# https://youtu.be/P00xJgWzz2c?list=PLAB1DA9F452D9466C
# f(n) = c + n x c x n x c x c x c x c x c
# o(n^2), theta(n^2), omega(n)


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
