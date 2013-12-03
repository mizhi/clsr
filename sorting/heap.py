class Heap(object):
    def __init__(self, elements):
        self.heap = elements
        self.heap_size = len(elements)
        self.build_heap()

    def build_heap(self):
        for i in range((len(self.heap) - 1) // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        # formula for left/right slightly different to compensate for
        # 0-based indexing in python
        left_subtree = 2 * i + 1
        right_subtree = 2 * i + 2

        largest = i
        if left_subtree < self.heap_size and \
           self.heap[left_subtree] > self.heap[i]:
            largest = left_subtree

        if right_subtree < self.heap_size and \
           self.heap[right_subtree] > self.heap[largest]:
            largest = right_subtree

        if largest != i:
            (self.heap[i], self.heap[largest]) = (self.heap[largest], self.heap[i])
            self.heapify(largest)
