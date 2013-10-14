# Insertion Sort, PG 17

def isort(l):
    l_c = l[:]
    for i in range(1, len(l_c)):
        v = l_c[i]
        j = i - 1
        while j >= 0 and l_c[j] > v:
            l_c[j+1] = l_c[j]
            j -= 1
        l_c[j+1] = v
    return l_c


import random
a = range(1,10)
random.shuffle(a)

print a
print isort(a)
