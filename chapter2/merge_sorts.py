# Insertion Sort, PG 29
#
# Not a 1-1 translation of the algorithm. In fact, there are 3 separate
# implementations. _merge_without_sentinel and _merge_with_sentinel
# both create a new list to hold the merged lists.
#
# _merge_inplace is closer to the CLSR version. The version in CLSR mutates the
# input list. That is, given a list A and indices indicating the left and right
# boundaries of the sublists, it would copy them into temporary lists, L and R,
# then merge those back into A.
#
# CLSR also employs the use of a sentinel value. This avoids the final two if
# statements in the merge. This works fine with integers, but would be a bit
# more difficult with arbitrary types. We can use None as our sentinel, but None
# < any integer in Python. To work around this, the code fills in the merged
# array from biggest to smallest rather than smallest to biggest. That is, it
# merges from right to left instead of left to right.

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






def merge_sort_inplace(unsorted_list, l = None, r = None):
    l = l or 0
    r = r or len(unsorted_list) - 1

    if l < r:
        m = (l + r) // 2
        merge_sort_inplace(unsorted_list, l, m)
        merge_sort_inplace(unsorted_list, m + 1, r)
        _merge_inplace(unsorted_list, l, m, r)
    return unsorted_list
