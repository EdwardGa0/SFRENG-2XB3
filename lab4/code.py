import timeit
from lab4 import *
from sorts import *

def timing_tests():
    f = open('./lab3/best_sort.txt', 'w')
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

def time_individual(i, sort_func):
    avg = []
    for _ in range(50):
        lst = create_near_sorted_list(1000, i/100)
        start = timeit.default_timer()
        sort_func(lst)
        end = timeit.default_timer()
        avg.append(end-start)
    return sum(avg)/len(avg)

def timing_tests_worstcase_comparison():
    f = open('./lab3/worst_case.txt', 'w')
    for i in range(0, 101, 5):
        print(i, end=' ')
        res = []
        res.append(time_individual(i, tri_pivot_quicksort))
        res.append(time_individual(i, bubble_sort))
        res.append(time_individual(i, selection_sort))
        res.append(time_individual(i, insertion_sort))
        f.write(str(i/100) + ', ' + ','.join(map(str, res)) + '\n')
    f.close()

#timing_tests_worstcase()

#for bottom-up vs top-down comparison
def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L
    
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

#runner()

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

three_way_test()
