import random
from isort import isort
from merge_sort import merge_sort

SORT_FUNCS = (merge_sort, isort)

class TestMergeSort(object):
    def setUp(self):
        self.pre_sort = range(1, 10)
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
        assert sort_func(range(9, 0, -1)) == range(1, 10)
