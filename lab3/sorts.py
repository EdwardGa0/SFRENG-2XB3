# dual pivot

# tri pivot

def tri_pivot_quicksort(L):
    copy = quicksort_copy(L, 3)
    for i in range(len(L)):
        L[i] = copy[i]

# quad pivot


# helper function
a = [4 * []]
for i in range(len(a)):
    print(len(a))

def multi_pivot_quicksort_copy(L, p):
    if len(L) < 2:
        return L
    pivots = L[:p]
    subarrays = [p * []]

