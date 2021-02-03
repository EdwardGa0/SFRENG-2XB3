import random
# dual pivot
def dual_pivot_quicksort(L):
    copy = mp_quicksort_copy(L, 2)
    for i in range(len(L)):
        L[i] = copy[i]

# tri pivot
def tri_pivot_quicksort(L):
    copy = mp_quicksort_copy(L, 3)
    for i in range(len(L)):
        L[i] = copy[i]

# quad pivot
def quad_pivot_quicksort(L):
    copy = mp_quicksort_copy(L, 4)
    for i in range(len(L)):
        L[i] = copy[i]

# helper function
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
e = [3,2]

dual_pivot_quicksort(a)
print(a)
dual_pivot_quicksort(b)
print(b)
dual_pivot_quicksort(c)
print(c)
dual_pivot_quicksort(d)
print(d)
dual_pivot_quicksort(e)
print(e)

#inplace quick sort
def quicksort_inplace(l, lo, hi): #lo starts at 0, hi is len(l)-1
    if hi <= lo: #base case
        return 

    pivot = partition(l, lo, hi) #does the sorting. 
    #returns the right position of the pivot value.

    quicksort_inplace(l, lo, pivot-1) #sort left elements
    quicksort_inplace(l, pivot+1, hi) #sort right elements
    
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
quicksort_inplace(lst, 0, len(lst)-1)
print(lst)
