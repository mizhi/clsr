import random
from insertion_sort import insertion_sort
from merge_sorts import (merge_sort_without_sentinel,
                         merge_sort_with_sentinel,
                         merge_sort_inplace)
from bubble_sort import bubblesort
from heap_sort import heap_sort


SORT_FUNCS = (merge_sort_without_sentinel, merge_sort_with_sentinel,
              merge_sort_inplace,
              insertion_sort,
              bubblesort,
              heap_sort)

INPLACE_SORT_FUNCS = (merge_sort_inplace, heap_sort)

class TestMergeSort(object):
    def setUp(self):
        self.odd_pre_sort = list(range(1, 10))
        self.reversed_odd = list(reversed(self.odd_pre_sort))
        random.shuffle(self.odd_pre_sort)

        self.even_pre_sort = list(range(1, 11))
        random.shuffle(self.even_pre_sort)

    def test_sorts(self):
        for sort_func in SORT_FUNCS:
            yield self.check_with_empty_list, sort_func
            yield self.check_with_random_list, sort_func
            yield self.check_with_reversed_list, sort_func

    def check_with_empty_list(self, sort_func):
        assert sort_func([]) == []

    def check_with_random_list(self, sort_func):
        assert sort_func(self.odd_pre_sort) == range(1, 10)
        assert sort_func(self.even_pre_sort) == range(1, 11)

    def check_with_reversed_list(self, sort_func):
        assert sort_func(self.reversed_odd) == range(1, 10)

    def test_inplace_sorts(self):
        for sort_func in INPLACE_SORT_FUNCS:
            yield self.check_inplace_sort_returns_same_list, sort_func

    def check_inplace_sort_returns_same_list(self, sort_func):
        sorted_list = sort_func(self.odd_pre_sort)
        assert id(sorted_list) == id(self.odd_pre_sort)
