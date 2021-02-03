import random
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

a = [4,1,4,5,6,7,2,3,4,1,5,5,3,1,7,8,8,5]
b = [1]
c = []
d = [1,2,3,4,5,6]
e = [3,2,1]

quad_pivot_quicksort(a)
print(a)
quad_pivot_quicksort(b)
print(b)
quad_pivot_quicksort(c)
print(c)
quad_pivot_quicksort(b)
print(d)
quad_pivot_quicksort(b)
print(e)

def timing_tests():
    f = open('./best_sort.txt', 'w')
    rand_lst = create_random_list(10000)
    for i in range(100, 10000, 100):
        res = []
        start = timeit.default_timer()
        my_quicksort(rand_lst[:i])
        end = timeit.default_timer()
        res.append(end - start)

        start = timeit.default_timer()
        dual_pivot_quicksort(rand_lst[:i])
        end = timeit.default_timer()
        res.append(end - start)

        start = timeit.default_timer()
        tri_pivot_quicksort(rand_lst[:i])
        end = timeit.default_timer()
        res.append(end - start)

        start = timeit.default_timer()
        quad_pivot_quicksort(rand_lst[:i])
        end = timeit.default_timer()
        res.append(end - start)

        f.write(str(i) + ', ' + ','.join(map(str, res)) + '\n')
    f.close()

def timing_tests_worstcase():
    f = open('./worst_case.txt', 'w')
    for i in range(0, 101):
        lst = create_near_sorted_list(1000, i/100)
        start = timeit.default_timer()
        dual_pivot_quicksort(lst)
        end = timeit.default_timer()
        f.write(str(i) + ', ' + str(end-start) + '\n')
    f.close()

#timing_tests()
timing_tests_worstcase()


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

#inplace sort test
lst = []
for i in range(30):
    lst.append(random.randint(0,50))
print(lst)
quicksort_inplace(lst)
print(lst)
