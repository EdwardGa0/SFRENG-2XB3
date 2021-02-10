import random

def mergesort_bottom(L):
    #merges list L, whose len is not always power of 2
    length = len(L)
    i = 1
    while(i < length): #i is the current size of sublists
        j = 0
        while(j < length-i): #j is the new size of the sublists
            merge_bottom(L, j, j+i-1, min(j+2*i-1, length-1))
            j += 2*i
        i = 2*i

def merge_bottom(L, start, mid, end):
    #helper func. Merge interval start-end 
    #assuming start-mid and mid-end are sorted.
    temp = L.copy() #temp list for comparison
    leftIndex = start
    rightIndex = mid+1
    
    for i in range(start, end+1):
        if(leftIndex > mid):
            L[i] = temp[rightIndex]
            rightIndex += 1
        elif(rightIndex > end):
            L[i] = temp[leftIndex]
            leftIndex += 1
        elif(temp[rightIndex] < temp[leftIndex]):
            L[i] = temp[rightIndex]
            rightIndex += 1
        else:
            L[i] = temp[leftIndex]
            leftIndex += 1

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L
    
ls = create_random_list(10)
mergesort_bottom(ls)
print(ls)