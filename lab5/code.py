from heap import Heap
import timeit
import random

def create_random_list(n):
    return [random.random() for _ in range(n)]

def time_test(n, runs):
    total = 0
    for _ in range(runs):
        L = create_random_list(n)
        start = timeit.default_timer()
        H = Heap(L)
        total += timeit.default_timer() - start
    return total/runs

for i in range(1000, 10000, 100):
    print(i, time_test(i, 10))