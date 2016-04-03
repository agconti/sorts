# https://youtu.be/P00xJgWzz2c?list=PLAB1DA9F452D9466C

def bubble_sort(items):
    number_of_sweeps_left = len(items) - 1
    while number_of_sweeps_left > 0:
        # one sweep
        for index, item in enumerate(items):

            if index >= number_of_sweeps_left:
                break

            next_item = items[index + 1]
            if item > next_item:
                items[index] = next_item
                items[index + 1] = item

        number_of_sweeps_left -= 1

    return items
