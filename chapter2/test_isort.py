import nose
import random
import unittest
from isort import isort

class ISortTests(unittest.TestCase):
    def setUp(self):
        self.pre_sort = range(1, 10)
        random.shuffle(self.pre_sort)

    def test_with_empty_list(self):
        assert isort([]) == []

    def test_with_random_list(self):
        assert isort(self.pre_sort) == range(1, 10)

    def test_with_reversed_list(self):
        assert isort(range(9, 0, -1)) == range(1, 10)
