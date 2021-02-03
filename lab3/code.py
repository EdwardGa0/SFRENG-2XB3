import timeit
from lab3 import *
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
    f = open('./lab3/worst_case.txt', 'w')
    for i in range(0, 101):
        avg = []
        for _ in range(100):
            lst = create_near_sorted_list(1000, i/100)
            start = timeit.default_timer()
            tri_pivot_quicksort(lst)
            end = timeit.default_timer()
            avg.append(end-start)
        f.write(str(i/100) + ', ' + str(sum(avg)/len(avg)) + '\n')
    f.close()

#timing_tests()
timing_tests_worstcase()