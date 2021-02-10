import random
from lab4 import merge

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

<<<<<<< HEAD
def merge_bottom_test(L, start, mid, end):
    #helper func. Merge interval start-end 
    #assuming start-mid and mid-end are sorted.
    temp = L[start:end+1].copy()
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

def mergesort_three(L):
    if len(L) <= 1:
        return 
    if len(L) == 2:
        if L[1] < L[0]:
            L[0], L[1] = L[1], L[0]
            return L
        else:
            return L

    lmid = len(L)//3
    rmid = lmid*2
    left, mid, right = L[:lmid], L[lmid:rmid], L[rmid:]

    #Mergesort core
    mergesort_three(left)
    mergesort_three(mid)
    mergesort_three(right)
    temp = merge_three(left, mid, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]

def merge_three(left, mid, right):
    return merge(merge(left, mid), right)

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L
    
L = create_random_list(1000)
after = L.copy()
mergesort_three(after)
if after != sorted(L):
    print(after)