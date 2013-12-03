from permute_sort import permute_by_sorting

class TestPermuteBySort(object):
    def setUp(self):
        self.pre_sort = list(range(1, 10))

    def test_permute(self):
        assert permute_by_sorting(self.pre_sort) != self.pre_sort
