#
# Maze Cell class
#

class Cell:
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
        return [self.cellNorth or None,
                self.cellSouth or None,
                self.cellWest or None,
                self.cellEast or None]

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
