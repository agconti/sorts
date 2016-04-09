# https://youtu.be/GCae1WNvnZM?list=PLAB1DA9F452D9466C
# http://visualgo.net/sorting.html


def merge_sort(items):
    if len(items) == 1:
        return items

    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(list_a, list_b):
    merged_array= []
    list_length = len(list_a)
    item_a = list_a.pop(0)
    item_b = list_b.pop(0)

    while len(merged_array) < (list_length * 2):

        if item_a < item_b:
            merged_array.append(item_a)

            try:
                item_a = list_a.pop(0)
            except IndexError:
                # we've fully sorted and added list a
                # add the remainder of sorted list b
                merged_array.append(item_b)
                merged_array += list_b

        if item_a > item_b:
            merged_array.append(item_b)

            try:
                item_b = list_b.pop(0)
            except IndexError:
                # we've fully sorted and added list b
                # add the remainder of sorted list a
                merged_array.append(item_a)
                merged_array += list_a

    return merged_array
