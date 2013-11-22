# Insertion Sort, PG 17

def isort(l):
    l_copy = l[:]
    for i in range(1, len(l_copy)):
        temp_value = l_copy[i]
        j = i - 1
        while j >= 0 and l_copy[j] > temp_value:
            l_copy[j+1] = l_copy[j]
            j -= 1
        l_copy[j+1] = temp_value
    return l_copy
