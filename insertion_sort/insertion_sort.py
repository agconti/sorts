# https://youtu.be/c4BRHC7kTaQ?list=PLAB1DA9F452D9466C
# http://visualgo.net/sorting.html


def insertion_sort(items):
    sorted_items = []

    for item in items:
        sort(item, sorted_items)

    return sorted_items


def sort(item, sorted_items):
    sorted_items.append(item)
    i = len(sorted_items)

    if len(sorted_items) == 0:
        return

    while i > 0:
        i -= 1

        if i == 0:
            break

        sorted_item = sorted_items[i]
        next_item = sorted_items[i - 1]
        if next_item < sorted_item:
            break

        swap(next_item, sorted_item, i, sorted_items)



def swap(left_item, right_item, index, items):
        items[index] = left_item
        items[index - 1] = right_item
