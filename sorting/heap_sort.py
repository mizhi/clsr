# Chapter 6, Heap Sort

from heap import Heap

def heap_sort(unsorted_list):
    h = Heap(unsorted_list)
    for i in range(len(unsorted_list) - 1, 0, -1):
        (h.heap[i], h.heap[0]) = (h.heap[0], h.heap[i])
        h.heap_size -= 1
        h.heapify(0)

    return unsorted_list
