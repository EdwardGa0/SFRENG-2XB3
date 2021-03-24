import math, random, timeit
from shortest_paths import *

def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G

#Assumes G represents its node as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G):
    n = G.number_of_nodes()
    d = [[999999 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i,j):
                d[i][j] = G.w(i,j)
        d[i][i] = 0
    return d

# Bellman-Ford approx testing
# total_d0 = 0
# total_d1 = 1
# k = 0
# while k <= 50:
#     start = timeit.default_timer()
#     G = create_random_complete_graph(50, 1000)
#     start = timeit.default_timer()
#     d0 = bellman_ford(G, 1)
#     t0 = timeit.default_timer() - start
#     total_d0 = total_dist(d0)
#     start = timeit.default_timer()
#     d1 = bellman_ford_approx(G, 1, k)
#     t1 = timeit.default_timer() - start
#     total_d1 = total_dist(d1)
#     print(t0, t1, total_d0, total_d1)
#     k += 1
