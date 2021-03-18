import random
import timeit
from mst import *

# prim vs prim
def test_prims():
    f = open('./prim_tests.txt', 'w')
    for i in range(100, 500, 2):
        g = create_random_connected_graph(50, i)
        start = timeit.default_timer()
        prim1(g)
        a = timeit.default_timer() - start
        start = timeit.default_timer()
        prim2(g)
        b = timeit.default_timer() - start
        f.write(str(i) + ', ' + str(a) + ', ' + str(b) + '\n')
    f.close()

def create_random_connected_graph(n, e):
    g = WeightedGraph(n)
    l = [i for i in range(1, e + 1)]
    for i in range(n - 1):
        g.add_edge(i, i + 1, l.pop(random.randint(0, len(l) - 1)))
    for i in range(e - n):
        n1 = random.randint(0, n - 1)
        n2 = random.randint(0, n - 1)
        while n2 != n1:
            n2 = random.randint(0, n - 1)
        g.add_edge(n1, n2, l.pop(random.randint(0, len(l) - 1)))
    return g

test_prims()