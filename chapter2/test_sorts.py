import random
from isort import isort
from merge_sorts import (merge_sort_without_sentinel,
                         merge_sort_with_sentinel,
                         merge_sort_inplace)


SORT_FUNCS = (merge_sort_without_sentinel, merge_sort_with_sentinel,
              merge_sort_inplace,
              isort)

class TestMergeSort(object):
    def setUp(self):
        self.pre_sort = list(range(1, 10))
        self.reversed_list = list(reversed(self.pre_sort))
        random.shuffle(self.pre_sort)

    def test_sorts(self):
        for sort_func in SORT_FUNCS:
            yield self.check_with_empty_list, sort_func
            yield self.check_with_random_list, sort_func
            yield self.check_with_reversed_list, sort_func

    def check_with_empty_list(self, sort_func):
        assert sort_func([]) == []

    def check_with_random_list(self, sort_func):
        assert sort_func(self.pre_sort) == range(1, 10)

    def check_with_reversed_list(self, sort_func):
        assert sort_func(self.reversed_list) == range(1, 10)

    def test_inplace_sort(self):
        sorted_list = merge_sort_inplace(self.pre_sort)
        assert id(sorted_list) == id(self.pre_sort)
