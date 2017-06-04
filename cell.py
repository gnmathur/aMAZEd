"""
Grid cell definition

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

class Cell:
    """
    Definition of a grid cell
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.cellNorth = None
        self.cellSouth = None
        self.cellWest = None
        self.cellEast = None
        self.links = dict()

    def link(self, cell, bidir=True):
        self.links[cell] = True
        if bidir == True:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidir=True):
        del self.links[cell]
        if bidir == True:
            cell.unlink(self, False)
        return self

    def getLinks(self):
        """
        Return all cells linked to this cell
        Returns: List of keys
        """
        return self.links.keys()

    def isLinked(self, cell):
        """
        Find out if <cell> is linked to this cell
        Returns: True, False
        """
        return cell in self.links

    def neighbors(self):
        n = []
        if self.cellNorth: n.append(self.cellNorth) 
        if self.cellSouth: n.append(self.cellSouth)
        if self.cellWest: n.append(self.cellWest)
        if self.cellEast: n.append(self.cellEast)
        return n

    def distances(self):
        """ This method computes the distance of each cell in the
        grid from <cell>
        """
        distances = Distances(self)
        frontier = [self]
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

    def __str__(self):
        s = "("+str(self.row)+", "+str(self.column)+")"
        return s

if __name__ == "__main__":
    c1 = Cell(0,0).link(Cell(1,1)).link(Cell(2,2))
    print c1.neighbors()
    for c2 in c1.getLinks():
        print c2, 
    print
    print Cell(1,1).neighbors()
