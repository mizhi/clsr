# Chapter 2, Insertion Sort, PG 38
#
# This, of course, is bubblesort.

def bubblesort(unsorted_list):
    l_copy = unsorted_list[:]
    for i in range(len(l_copy)):
        for j in range(i, len(l_copy)):
            if l_copy[i] > l_copy[j]:
                l_copy[i], l_copy[j] = l_copy[j], l_copy[i]
    return l_copy
