# Permute By Sorting, PG 101

import random

def permute_by_sorting(list_1):
    elements_probs = []
    for i in range(0, len(list_1)):
        elements_probs.append((list_1[i],
                               random.randint(1, len(list_1)**3)))
    shuffled_list = sorted(elements_probs, key = lambda _x: _x[1])
    return [_x[0] for _x in shuffled_list]
