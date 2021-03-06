import timeit
from lab3 import *

# dual pivot
def dual_pivot_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

# tri pivot
def tri_pivot_quicksort(L):
    copy = tri_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

# quad pivot
def quad_pivot_quicksort(L):
    copy = quad_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]
        
# dual helper
def dual_quicksort_copy(L):
    if len(L) < 2:
        return L
    p1 = min(L[0], L[1])
    p2 = max(L[0], L[1])
    if len(L) < 3:
        return [p1, p2]

    l1, l2, l3 = [], [], []

    for num in L[2:]:
        if num < p1:
            l1.append(num)
        elif num < p2:
            l2.append(num)
        else:
            l3.append(num)
    return dual_quicksort_copy(l1) + [p1] + dual_quicksort_copy(l2) + [p2] + dual_quicksort_copy(l3)

# tri helper
def tri_quicksort_copy(L):
    if len(L) < 2:
        return L
    elif len(L) < 3:
        return [min(L[0], L[1]), max(L[0], L[1])]
    s = L[0] + L[1] + L[2]
    p1 = min(L[0], L[1], L[2])
    p3 = max(L[0], L[1], L[2])
    p2 = s - p1 - p3
    l1, l2, l3, l4 = [], [], [], []

    for num in L[3:]:
        if num < p1:
            l1.append(num)
        elif num < p2:
            l2.append(num)
        elif num < p3:
            l3.append(num)
        else:
            l4.append(num)
    output = tri_quicksort_copy(l1) + [p1] + tri_quicksort_copy(l2) + [p2]
    output += tri_quicksort_copy(l3) + [p3] + tri_quicksort_copy(l4)
    return output

# quad helper
def quad_quicksort_copy(L):
    if len(L) < 2:
        return L
    elif len(L) < 3:
        return [min(L[0], L[1]), max(L[0], L[1])]
    elif len(L) < 4:
        s = L[0] + L[1] + L[2]
        p1 = min(L[0], L[1], L[2])
        p3 = max(L[0], L[1], L[2])
        p2 = s - p1 - p3
        return [p1, p2, p3]

    min1 = min(L[0], L[1])
    max1 = max(L[0], L[1])
    min2 = min(L[2], L[3])
    max2 = max(L[2], L[3])
    p1 = min(min1, min2)
    p4 = max(max1, max2)
    p2 = min(min1 + min2 - p1, max1 + max2 - p4)
    p3 = max(min1 + min2 - p1, max1 + max2 - p4)
    l1, l2, l3, l4, l5 = [], [], [], [], []

    for num in L[4:]:
        if num < p1:
            l1.append(num)
        elif num < p2:
            l2.append(num)
        elif num < p3:
            l3.append(num)
        elif num < p4:
            l4.append(num)
        else:
            l5.append(num)
    output = quad_quicksort_copy(l1) + [p1] + quad_quicksort_copy(l2) + [p2]
    output += quad_quicksort_copy(l3) + [p3] + quad_quicksort_copy(l4) + [p4] + quad_quicksort_copy(l5)
    return output

# dynamic function for any number of pivots
def mp_quicksort_copy(L, p):
    if len(L) < 2:
        return L
    pivots = mp_quicksort_copy(L[:p], 1)
    if len(L) < p:
        return pivots

    subarrays = [[] for i in range(p + 1)]

    for num in L[p:]:
        found = False
        for i in range(p):
            if num < pivots[i]:
                subarrays[i].append(num)
                found = True
                break
        if not found:
            subarrays[p].append(num)

    finalSorted = []
    for i in range(p):
        finalSorted += mp_quicksort_copy(subarrays[i], p) + [pivots[i]]
    finalSorted += mp_quicksort_copy(subarrays[p], p)
    return finalSorted

# elementary sorts
def bubble_sort(L):
    for i in range(len(L) - 1):
        swapped = False
        for j in range(len(L) - i - 1):
            if L[j + 1] < L[j]:
                swapped = True
                L[j], L[j + 1] = L[j + 1], L[j]
        if not swapped:
            break

def selection_sort(L):
    for i in range(len(L)):
        m = i
        for j in range(i + 1, len(L)):
            if L[j] < L[m]:
                m = j
        L[i], L[m] = L[m], L[i]

def insertion_sort(L):
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j] < L[j - 1]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1

def final_sort(L):
    if len(L) < 13:
        insertion_sort(L)
    else:
        tri_pivot_quicksort(L)

#inplace quick sort

def quicksort_inplace(l):
    quicksort_helper(l, 0, len(l)-1)

def quicksort_helper(l, lo, hi):
    if hi <= lo: #base case
        return 

    pivot = partition(l, lo, hi) #does the sorting. 
    #returns the right position of the pivot value.

    quicksort_helper(l, lo, pivot-1) #sort left elements
    quicksort_helper(l, pivot+1, hi) #sort right elements
    
def partition(l, lo, hi):
    pivot = l[hi] #pivot is always at the end.

    small = lo #position where smaller values will be placed

    for element in range(lo, hi): #not including hi (pivot)
        if l[element] < pivot:
            l[small], l[element] = l[element], l[small]
            small += 1

    l[small], l[hi] = l[hi], l[small] #put pivot on the right spot
    return small

