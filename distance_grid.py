"""
Grid definition

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

from distance import Distances
from grid import Grid

class DistanceGrid(Grid):
    def distances(self, cell):
        """ This method computes the distance of each cell in the
        grid from <cell>
        """
        distances = Distances(cell)
        frontier = [cell]
        while len(frontier) > 0:
            new_frontier = []
            for cell in frontier:
                for linked_cell in cell.getLinks():
                    if distances[linked_cell] != None:
                        continue
                    distances[linked_cell] = distances[cell] + 1
                    new_frontier.append(linked_cell)
            frontier = new_frontier
        return distances

    def path_to(self, goal):
        current = goal
        root = self[0,0]
        d = self.distances(root)
        crumbs = Distances(root)
        crumbs[current] = d[current]

        while current is not root:
            for neighbor in current.getLinks():
                if d[neighbor] < d[current]:
                    crumbs[neighbor] = d[neighbor]
                    current = neighbor
        return crumbs

    def draw_ascii(self):
        """ Draw the ASCII maze with distance information
        This method always computes the distance from the root set at (0, 0)
        """
        distances = self.distances(self[0,0])
        output = '+' + "---+" * self.columns + '\n'
        for row in self.each_row():
            top = '|'
            bottom = '+'
            for cell in row:
                body = '{:3d}'.format(distances[cell])
                east_boundary = ' ' if cell.isLinked(cell.cellEast) else '|'
                top = top + body + east_boundary
                south_boundary = '   ' if cell.isLinked(cell.cellSouth) else '---'
                corner = '+'
                bottom = bottom + south_boundary + corner
            output = output + top + '\n'
            output = output + bottom + '\n'
        print output
                
if __name__ == "__main__":
    """
    Unit tests
    """
    pass
