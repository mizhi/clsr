import random
from heap import Heap

class TestHeap(object):
    def setUp(self):
        self.odd_pre_heap = list(range(1, 10))
        random.shuffle(self.odd_pre_heap)

        self.even_pre_heap = list(range(1, 11))
        random.shuffle(self.even_pre_heap)

    def test_heap(self):
        h = Heap(self.odd_pre_heap)
