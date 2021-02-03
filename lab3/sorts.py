import random
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
    pivot = L[:p]
    subarrays = [p * []]

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
