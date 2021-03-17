import random
from graphs import *

def create_random_graph(num_nodes, num_edges):
    G = Graph(num_nodes)
    for i in range(num_edges):
        a = random.randint(0, num_nodes-1)
        b = random.randint(0, num_nodes-1)
        G.add_edge(a, b)
    return G

def cycle_vs_c():
    runs = 1000
    for i in range(100):
        count = 0
        for j in range(runs):
            G = create_random_graph(100, i)
            if has_cycle(G):
                count += 1
        print(i, count/runs)

def connected_vs_c():
    runs = 100
    for i in range(0, 1000, 10):
        count = 0
        for j in range(runs):
            G = create_random_graph(100, i)
            if is_connected(G):
                count += 1
        print(i, count/runs)

connected_vs_c()