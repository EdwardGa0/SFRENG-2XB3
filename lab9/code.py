import math

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

def test_mystery():
    f = open('./mystery_tests.txt', 'w')
    for i in range(1, 1000):
        G = create_random_complete_graph(i, 1000)
        start = timeit.default_timer()
        mystery(G)
        a = timeit.default_timer() - start
        f.write(str(i) + ', ' + str(a) + '\n')
    f.close()

G = create_random_complete_graph(3, 5)
print(G.weights)
print(all_pairs_dijkstra(G))
print(all_pairs_bellman_ford(G))
test_mystery()
