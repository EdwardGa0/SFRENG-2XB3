from collections import deque

# Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()

# BFS 2
def BFS2(G, node1, node2):
    Q = deque()
    Q.append([node1])
    visited = set()
    while Q:
        path = Q.popleft()
        node = path[-1]
        visited.add(node)
        if node == node2:
            return path
        for adj in G.adj[node]:
            if adj not in visited:
                new_path = path.copy()
                new_path.append(adj)
                Q.append(new_path)
    return []

# DFS 2
def DFS2(g, n1, n2):
    return DFS2recur(g, n1, n2, [False for _ in range(len(g.adj))], [n1])

def DFS2recur(g, n1, n2, vis, l):
    if n1 == n2:
        return l
    o = []
    if not vis[n1]:
        vis[n1] = True
        for node in g.adj[n1]:
            if not vis[node]:
                l.append(node)
                o = DFS2recur(g, node, n2, vis, l)
                if len(o) > 0:
                    return o
                l.pop()
    return o

# BFS 3
def BFS3(G, node):
    path = {}
    Q = deque([node])
    marked = {node: True}
    for nodes in G.adj:
        if nodes != node:
            marked[nodes] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for nodes in G.adj[current_node]:
            if not marked[nodes]:
                Q.append(nodes)
                marked[nodes] = True
                path[nodes] = current_node
    return path

# DFS 3
def DFS3(G, start):
    visited = set()
    pred = {}
    DFS3_rec(G, start, visited, pred)
    return pred

def DFS3_rec(G, node, visited, pred):
    visited.add(node)
    for adj in G.adj[node]:
        if adj not in visited:
            pred[adj] = node
            DFS3_rec(G, adj, visited, pred)

# has_cycle
def has_cycle(g):
    for i in range(len(g.adj)):
        s = [i]
        vis = [False for _ in range(len(g.adj))]
        while len(s) != 0:
            cur = s.pop()
            if not vis[cur]:
                vis[cur] = True
                c = 0
                for node in g.adj[cur]:
                    if vis[node]:
                        c += 1
                    else:
                        s.append(node)
                if c > 1:
                    return True
    return False

# is connected; uses BFS
def is_connected(G):
    for node1 in range(len(G.adj)):
        for node2 in range(len(G.adj)):
            if node1 == node2 or BFS(G, node1, node2):
                continue
            else:
                return False
    return True

def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


# g = Graph(6)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(3,4)
# g.add_edge(4,5)

# print(BFS2(g,1,5))
# print(DFS2(g,1,5))
# print(BFS3(g,1))
# print(DFS3(g,1))
# print(has_cycle(g))
# print(is_connected(g))
