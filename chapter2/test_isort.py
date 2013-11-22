import nose
import random
from isort import isort


pre_sort = None
def setup_func():
    global pre_sort
    pre_sort = range(1, 10)
    random.shuffle(pre_sort)

@nose.with_setup(setup_func)
def test_isort():
    assert isort(pre_sort) == range(1, 10)
