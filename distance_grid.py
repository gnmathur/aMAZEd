"""
Distance-Grid definition

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

from grid import Grid
from distance import Distances

class DistanceGrid(Grid):
    """ A distance grid is a specialized grid that is capable of computing 
    distances between cells.
    """

    def __init__(self, nRows, nColumns):
        super(DistanceGrid, self).__init__(nRows, nColumns)
        self.distances = None

    def compute_distances(self, start):
        """ This method computes the distance of each cell in the
        grid from <start>

        The implementation uses Dijkstra's algorithm to compute the distances.
        """
        self.distances = Distances(start)
        frontier = [start]
        while len(frontier) > 0:
            new_frontier = []
            for cell in frontier:
                for linked_cell in cell.getLinks():
                    if self.distances[linked_cell] != None:
                        continue
                    self.distances[linked_cell] = self.distances[cell] + 1
                    new_frontier.append(linked_cell)
            frontier = new_frontier
        return self.distances

    def solve(self, start, goal):
        """ This method computes the shortest path from <start> to <goal> """
        self.compute_distances(start)

        current = goal
        crumbs = Distances(start)

        crumbs[current] = self.distance[current]

        while current is not goal:
            for neighbor in current.getLinks():
                if self.distance[neighbor] < self.distance[current]:
                    crumbs[neighbor] = self.distances[neighbor]
                    current = neighbor
        return crumbs

    def contents_of(self, cell):
        """ This routine prints the contents of this cell. This overloaded 
        function defines the contents of this cell as the distance of this cell 
        from some defined root cell 
        """
        if self.distances is not None:
            return str(self.distances[cell])
        else:
            return super(DistanceGrid, self).contents_of()
                
if __name__ == "__main__":
    """
    Unit tests
    """
    pass
