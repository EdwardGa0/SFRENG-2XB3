import math
import timeit

# min heap
class MinHeap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.map = {}
        for i in range(len(L)):
            self.map[L[i].value] = i
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        smallest_known = i
        if self.left(i) < self.length and self.data[self.left(i)].key < self.data[i].key:
            smallest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)].key < self.data[smallest_known].key:
            smallest_known = self.right(i)
        if smallest_known != i:
            self.data[i], self.data[smallest_known] = self.data[smallest_known], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[smallest_known].value] = smallest_known
            self.sink(smallest_known)

    def insert(self, element):
        if len(self.data) == self.length:
            self.data.append(element)
        else:
            self.data[self.length] = element
        self.map[element.value] = self.length
        self.length += 1
        self.swim(self.length - 1)

    def insert_elements(self, L):
        for element in L:
            self.insert(element)

    def swim(self, i):
        while i > 0 and self.data[i].key < self.data[self.parent(i)].key:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[self.parent(i)].value] = self.parent(i)
            i = self.parent(i)

    def get_min(self):
        if len(self.data) > 0:
            return self.data[0]
  
    def extract_min(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        self.map[self.data[self.length - 1].value] = self.length - 1
        self.map[self.data[0].value] = 0
        min_element = self.data[self.length - 1]
        self.length -= 1
        self.map.pop(min_element.value)
        self.sink(0)
        return min_element

    def decrease_key(self, value, new_key):
        if new_key >= self.data[self.map[value]].key:
            return
        index = self.map[value]
        self.data[index].key = new_key
        self.swim(index)

    def get_element_from_value(self, value):
        return self.data[self.map[value]]

    def is_empty(self):
        return self.length == 0
    
    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# element class
class Element:
    def __init__(self, value, key):
        self.value = value
        self.key = key

    def __str__(self):
        return "(" + str(self.value) + "," + str(self.key) + ")"


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

# prim 2
def prim2(G):
    n = G.number_of_nodes()
    mst = WeightedGraph(n)
    INF = 1e9
    heap = MinHeap([Element(i, INF) for i in range(n)])
    
    visited = [False] * n

    for _ in range(n):
        u = heap.extract_min()
        visited[u.value] = True
        added = False
        for v, w in G.adjacent_nodes(u.value):
            if not visited[v]:
                heap.decrease_key(v, w)
            elif u.key == G.w(u.value, v) and not added:
                # assuming all weights are unique
                mst.add_edge(u.value, v, u.key)
                added = True
    return mst


# prim vs prim
def test_prims():
    f = open('./prim_tests.txt', 'w')
    for i in range(0, 800, 2):
        g = create_random_connected_graph(i)
        start = timeit.default_timer()
        prim1(g)
        a = timeit.default_timer() - start
        start = timeit.default_timer()
        prim2(g)
        b = timeit.default_timer() - start
        f.write(str(i) + ', ' + str(a) + ', ' + str(b) + '\n')
    f.close()

def create_random_connected_graph(n):
    g = WeightedGraph(n)
    l = [i for i in range(1, n + 1)]
    for i in range(n):
        g.add_edge(i, i + 1, l.pop(random.randint(len(l))))
    return g


# tests
g = WeightedGraph(6)
# g.add_edge(0, 1, 3)
# g.add_edge(1, 2, 8)
# g.add_edge(0, 2, 8)
g.add_edge(0,1,5)
g.add_edge(0,2,6)
g.add_edge(1,4,10)
g.add_edge(1,3,7)
g.add_edge(1,2,4)
g.add_edge(0,5,3)
g.add_edge(4,5,1)
g.add_edge(3,5,9)

print(prim1(g).adj)