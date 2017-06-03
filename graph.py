#!/usr/bin/env python
"""
Graph implementation

MIT License

Copyright (c) 2017 Gaurav Mathur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

class Edge:
    """
    Graph edge representation
    """
    def __init__(self, node_from, node_to, weight, directed):
        self.weight = weight
        self.node_from = node_from
        self.node_to = node_to
        node_from.add_neighbor(self)
        if not directed:
            node_to.add_neighbor(self)

    # Edge methods
    def get_nodes(self):
        return node_from, node_to

class Node:
    def __init__(self, pld):
        self.pld = pld
        self.edges = set()

    def add_neighbor(self, edge):
        self.edges.add(edge)

    def each_neighbor(self):
        for edge in self.edges:
            yield edge.node_to if edge.node_from is self else edge.node_from

    # Factory method
    @staticmethod
    def create(*nIds):
        """ Create N Node instances
        
        Argument:
        nIds - A list of N identifiers. Create a Node instance for each of these
        """
        nodes = []
        for nId in nIds:
            nodes.append(Node(nId))
        return nodes

    def __str__(self):
        return str(self.pld)

class Graph:
    """
    Graph class
    """
    # Graph methods
    def __init__(self, directed=True):
        """ Create a graph object
        Keyword Arguments:
        directed - set to False for undirected graphs
        """
        self.nodes = set()
        self.edges = []
        self.directed = directed
    
    def add_edge(self, node_from, node_to, weight=0):
        """ Add an edge to the graph
        Positional Arguments:
        node_from - draw an edge from this node
        node_to - draw an edge to this node

        Keyword Arguments:
        weight - edge weight
        """
        self.edges.append(Edge(node_from, node_to, weight, self.directed))
        self.nodes.update([node_from, node_to])
        return self

    def each_node(self):
        for node in self.nodes:
            yield node

    def each_edge(self):
        for node in each_edge():
            yield edge

    def dfs(self, start_node, cbfunc):
        """ Depth-first implementation
    
        This is an iterative implementation. A consequence of that is that it
        might not be possible to get 'number of descendents' information in
        this implementation.

        Positional arguments:
        start_node - Node to start the search from
        cbfunc - Callback function to call when a Node is discovered in the 
                graph
        """
        visited = set()
        stack = [start_node]

        while len(stack) != 0:
            node = stack.pop()
            if node in visited:
                continue
            cbfunc(node)
            visited.add(node)
            for neighbor_node in node.each_neighbor():
                stack.append(neighbor_node)

    def bfs(self, start_node, visit_func, distance_func = None):
        """ Breadth first search implementation

        Breadth-first search on a graph. This implementation also computes the
        distance of a node from the start node.

        Positional Arguments -
        start_node - node to start the search from
        visit_func - this function will be called when a new node is discovered in the search

        Keywork Arguments - 
        distance_func - this function will be called with an argument that includes all the 
                        computed distances
        """
        from collections import deque

        distances = dict()
        distances[start_node] = 0
        visited = set()
        qu = deque()
        qu.appendleft(start_node)
        while len(qu) != 0:
            node = qu.pop()
            if node in visited:
                continue
            visit_func(node)
            visited.add(node)
            for neighbor_node in node.each_neighbor():
                qu.appendleft(neighbor_node)
                if neighbor_node not in distances.keys():
                    distances[neighbor_node] = distances[node] + 1
        if distance_func:
            distance_func(distances)

if __name__ == "__main__":
    g = Graph()
    nA, nB, nC, nD, nE, nF, nG, nH, nI = \
        Node.create('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')

    #                        +----+
    #                +-------+  A +------+
    #                |       +----+      |
    #                |                   |
    #                |                   |
    #              +-v--+              +-v--+
    # +------------>  B |              |  C +----------+
    # |            +-+--+              +-+--+          |
    # |              |                   |             |
    # |       +----+ |                +--v-+        +--v-+
    # |       |    | |                |  E |        |    |
    # |       | D  <-+                |    +-------->   F|
    # |       +-+--+                  +-^--+        +--+-+
    # |         |                       |              |
    # |         |                       |              |
    # |       +-v--+                    |           +--v-+
    # |       |    |                    |           |  G |
    # |       | H  +--------------------+           +----+
    # |       +-+--+                                
    # |         |
    # |         |
    # |       +-v--+
    # +-------+ I  |
    #         +----+
    g.add_edge(nA, nB).add_edge(nA, nC).add_edge(nB, nD).add_edge(nD, nC)
    g.add_edge(nC, nE).add_edge(nC, nF).add_edge(nF, nG).add_edge(nE, nF)
    g.add_edge(nD, nH).add_edge(nH, nI).add_edge(nI, nB).add_edge(nH, nE)
    
    print "Neighbors of 'C':", 
    for neigh in nC.each_neighbor():
        print neigh,
    print

    def printthis(X): print X,

    print "DFS (root=A):", 
    g.dfs(nA, printthis)
    print

    print "DFS (root=C):", 
    g.dfs(nC, printthis)
    print

    def distancesprint(distance_dict):
        print
        for key, value in distance_dict.items():
            print key, "-->", value

    print "BFS (root=A):",
    g.bfs(nA, printthis, distancesprint)
    print
