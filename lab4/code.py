import timeit
from lab4 import *
from sorts import *

# for testing worst case
def timing_tests_worstcase():
    f = open('./worst_case.txt', 'w')
    for i in range(0, 51):
        avg = []
        for _ in range(100):
            lst = create_near_sorted_list(500, i/100)
            start = timeit.default_timer()
            mergesort(lst)
            end = timeit.default_timer()
            avg.append(end-start)
        f.write(str(i/100) + ', ' + str(sum(avg)/len(avg)) + '\n')
    f.close()

#for bottom-up vs top-down comparison
def test_helper(n):
    total = 0
    for i in range(50):
        ls = create_random_list(n)
        start = timeit.default_timer()
        mergesort_bottom(ls)
        end = timeit.default_timer()
        total += end - start
    print(total/50)

def runner():
    for i in range(1000,10001,500):
        print(i, end=" ")
        test_helper(i)

#three way comparison
def three_way_test():
    for i in range(1000, 10000, 1000):
        L1 = create_random_list(i)
        L2 = L1.copy()
        start = timeit.default_timer()
        mergesort_bottom(L1)
        end = timeit.default_timer()
        t1 = end - start
        start = timeit.default_timer()
        mergesort_three(L1)
        end = timeit.default_timer()
        t2 = end - start
        print(t1, t2)
