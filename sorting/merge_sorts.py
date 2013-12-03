# Chapter 2, Merge Sort, PG 29
#
# There are 3 separate implementations of merge sort, each playing with
# different ways of implementing the merge step.
#
# _merge_without_sentinel and _merge_with_sentinel both create a new list to
# hold the merged lists. _merge_without_sentinel is how I would most likely
# implement merge sort the first go around. It seems the most obvious way of
# implementing it in Python, though maybe not the most efficient.
#
# _merge_with_sentinel was motivated by the way CLSR uses sentinels to detect
# that a list has no more elements to merge. The implementation in CLSR assumes
# integers, and in order to accomodate other datatypes, you would have to have
# some value that is greater than everything. A simpler solution is to use None,
# which is less than everything in Python2 (Python3 "fixed" this feature, so
# I will need to figure out a new strategy).  In any case, by adopting this
# convention, we need to merge from largest to smallest and the indices are
# initialized and updated accordingly.
#
# _merge_inplace is closest to the CLSR implementation. The version in CLSR
# mutates the input list. That is, given a list A and indices indicating the
# left and right boundaries of the sublists, it would copy them into temporary
# lists, L and R, then merge those back into A. _merge_inplace follows this
# algorithm with the following differences.
#
# 1) CLSR arrays are 1-based indexed and the last index is typically the last
#    element of the list. Python is 0-based and the last index is one past the
#    last element of the list. We compensate accordingly.
# 2) We allow l and r to go unspecified to ease the initial call to
#    merge_sort_inplace

def _merge_without_sentinel(list_1, list_2):
    i = 0
    j = 0
    merged = []

    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            merged.append(list_1[i])
            i += 1
        else:
            merged.append(list_2[j])
            j += 1

    if i < len(list_1):
        merged.extend(list_1[i:])

    if j < len(list_2):
        merged.extend(list_2[j:])

    return merged

def _merge_with_sentinel(list_1, list_2):
    temp_list_1 = [None] + list_1
    temp_list_2 = [None] + list_2

    i = len(temp_list_1) - 1
    j = len(temp_list_2) - 1
    merged = [None] * (len(list_1) + len(list_2))
    k = len(merged) - 1
    while (temp_list_1[i] is not None) or (temp_list_2[j] is not None):
        if temp_list_1[i] > temp_list_2[j]:
            merged[k] = temp_list_1[i]
            i -= 1
        else:
            merged[k] = temp_list_2[j]
            j -= 1
        k -= 1

    return merged

def _merge_sort(unsorted_list, merge_func):
    if len(unsorted_list) == 0 or len(unsorted_list) == 1:
        return unsorted_list

    left = unsorted_list[:len(unsorted_list)//2]
    right = unsorted_list[len(unsorted_list)//2:]

    sorted_left = _merge_sort(left, merge_func)
    sorted_right = _merge_sort(right, merge_func)
    return merge_func(sorted_left, sorted_right)

def merge_sort_without_sentinel(unsorted_list):
    return _merge_sort(unsorted_list, _merge_without_sentinel)

def merge_sort_with_sentinel(unsorted_list):
    return _merge_sort(unsorted_list, _merge_with_sentinel)


def _merge_inplace(unsorted_list, l, m, r):
    l_copy = [None] + unsorted_list[l:m]
    r_copy = [None] + unsorted_list[m:r]
    i = len(l_copy) - 1
    j = len(r_copy) - 1
    k = r - 1
    while (l_copy[i] is not None) or (r_copy[j] is not None):
        if l_copy[i] < r_copy[j]:
            unsorted_list[k] = r_copy[j]
            j -= 1
        else:
            unsorted_list[k] = l_copy[i]
            i -= 1
        k -= 1

def merge_sort_inplace(unsorted_list, l = None, r = None):
    if l is None:
        l = 0

    if r is None:
        r = len(unsorted_list)

    m = (l + r) // 2

    if l < r - 1:
        merge_sort_inplace(unsorted_list, l, m)
        merge_sort_inplace(unsorted_list, m, r)
        _merge_inplace(unsorted_list, l, m, r)
    return unsorted_list
