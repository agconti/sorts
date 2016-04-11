# https://youtu.be/6NB0GHY11Iw?list=PLAB1DA9F452D9466C
# http://visualgo.net/sorting.html
import heapq


def heap_sort(items):
    heap = list(items)
    heapq.heapify(heap)

    return [heapq.heappop(heap) for i in range(len(heap))]
