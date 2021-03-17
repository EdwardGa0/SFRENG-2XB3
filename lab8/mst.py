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

