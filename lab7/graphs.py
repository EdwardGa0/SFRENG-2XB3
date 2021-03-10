from collections import deque

def DFS2(g, n1, n2):
    vis = [False for _ in range(g.number_of_nodes())]
    return DFS2recur(g, n1, n2, vis, [n1])

def DFS2recur(g, n1, n2, vis, l):
    if n1 == n2:
        return l
    o = []
    if vis[n1] == False:
        vis[n1] = True
        for node in g.adj[n1]:
            if vis[node] == False:
                l.append(node)
                o = DFS2recur(g, node, n2, vis, l)
                if len(o) > 0:
                    return o
                l.pop()
    return o

#Undirected graph using an adjacency list
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

    def number_of_nodes(self):
        return len(self.adj)

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print(DFS2(g, 0, 4))
