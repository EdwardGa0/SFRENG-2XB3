from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n+1):
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

def BSF3(G, node):
    path = {}
    Q = deque([node])
    marked = {node : True}
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




# g = Graph(6)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(3,4)
# g.add_edge(3,5)
# g.add_edge(5,4)
# g.add_edge(4,6)

# print(BFS2(g,1,5))

