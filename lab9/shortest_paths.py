def all_pairs_dijkstra(G):
    matrix = []
    nodes = list(G.adj.keys())
    for src in nodes:
        matrix.append(list(dijkstra(G, src).values()))
    return matrix


def all_pairs_bellman_ford(G):
    matrix = []
    nodes = list(G.adj.keys())
    for src in nodes:
        matrix.append(list(bellman_ford(G, src).values()))
    return matrix
