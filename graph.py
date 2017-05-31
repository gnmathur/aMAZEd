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
        Positional arguments:
        start_node - Node to start the search from
        cbfunc - Callback function to call when a Node is discovered in the 
                graph
        """
        visited = set()
        stack = [start_node]
        while len(stack) != 0:
            n = stack.pop()
            if n in visited:
                continue
            cbfunc(n)
            visited.add(n)
            for neighbor in n.each_neighbor():
                stack.append(neighbor)


if __name__ == "__main__":
    g = Graph()
    nA = Node('A') 
    nB = Node('B') 
    nC = Node('C') 
    nD = Node('D') 
    nE = Node('E') 
    nF = Node('F') 
    nG = Node('G') 
    nH = Node('H') 
    nI = Node('I')

    g.add_edge(nA, nB).add_edge(nA, nC)
    g.add_edge(nB, nD).add_edge(nD, nC)
    g.add_edge(nC, nE).add_edge(nC, nF)
    g.add_edge(nF, nG).add_edge(nE, nF)
    g.add_edge(nD, nH).add_edge(nH, nI).add_edge(nI, nB)
    
    print "Neighbors of 'C':", 
    for neigh in nC.each_neighbor():
        print neigh,
    print
    print "DFS:", 
    def printthis(X): print X,
    g.dfs(nA, printthis)

