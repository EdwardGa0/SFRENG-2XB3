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

def timing_tests_small_lists():
    f = open('./small_lists.txt', 'w')
    for j in range(0, 21):
        q = []
        b = []
        i = []
        s = []
        for _ in range(100):
            l = create_random_list(j)
            lst = l.copy()
            start = timeit.default_timer()
            tri_pivot_quicksort(lst)
            end = timeit.default_timer()
            q.append(end-start)

            lst = l.copy()
            start = timeit.default_timer()
            bubble_sort(lst)
            end = timeit.default_timer()
            b.append(end-start)

            lst = l.copy()
            start = timeit.default_timer()
            insertion_sort(lst)
            end = timeit.default_timer()
            i.append(end-start)
            
            lst = l.copy()
            start = timeit.default_timer()
            selection_sort(lst)
            end = timeit.default_timer()
            s.append(end-start)
        out = str(j) + ', ' + str(sum(q)/len(q)) + ', ' + str(sum(b)/len(b)) + ', ' 
        out += str(sum(i)/len(i)) + ', ' + str(sum(s)/len(s)) + '\n' 
        f.write(out)
    f.close()

#timing_tests()
#timing_tests_worstcase()
timing_tests_small_lists()

def test_helper(n):
    total = 0
    for i in range(25):
        ls = create_random_list(n)
        start = timeit.default_timer()
        tri_pivot_quicksort(ls)
        end = timeit.default_timer()
        total += end - start
    print(total/25)

def runner():
    for i in range(1000,10001,50):
        print(i, end=" ")
        test_helper(i)

#runner()

def worst_case_test_helper(n):
    ls = create_near_sorted_list(n, 0)
    start = timeit.default_timer()
    tri_pivot_quicksort(ls)
    end = timeit.default_timer()
    print(end-start)

def runner2():
    for i in range(1000,10001,500):
        print(i, end=" ")
        worst_case_test_helper(i)

#runner2()
