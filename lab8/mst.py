#Undirected graph using an adjacency list
class WeightedGraph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        for edge in self.adj[node1]:
            if edge[0] == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2, weight):
        if node1 not in self.adj[node2]:
            self.adj[node1].append((node2, weight))
            self.adj[node2].append((node1, weight))

    def w(self, node1, node2):
        for edge_info in self.adj[node1]:
            if node2 == edge_info[0]:
                return edge_info[1]

    def number_of_nodes(self):
        return len(self.adj)

#uses WeightedGraph
def prim1(G):
    mst = WeightedGraph(G.number_of_nodes())

    visited = [0]

    for _ in range(G.number_of_nodes()-1):
        minimum = 1001
        min_node = None
        attach_to = None
        for curr_node in visited:
            for adj_node in [x[0] for x in G.adjacent_nodes(curr_node)]:
                if not(adj_node in visited) and G.w(curr_node, adj_node) < minimum:
                    minimum = G.w(curr_node, adj_node)
                    min_node = adj_node
                    attach_to = curr_node
        visited.append(min_node)
        mst.add_edge(min_node, attach_to, minimum)

    return mst

g = WeightedGraph(6)
g.add_edge(0,1,5)
g.add_edge(0,2,6)
g.add_edge(1,4,10)
g.add_edge(1,3,7)
g.add_edge(1,2,4)
g.add_edge(0,5,3)
g.add_edge(4,5,1)
g.add_edge(3,5,9)

print(prim1(g).adj)
