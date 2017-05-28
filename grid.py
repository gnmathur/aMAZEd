#
# Maze Grid class
#

from cell import Cell
import random

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def size(self):
        return rows*columns

    def prepare_grid(self):
        grid = [[Cell(row, col) for col in range(self.columns)] for row in range(self.rows)]
        return grid

    def each_row(self):
        """
        Iterate over each row in the grid
        """
        for row in self.grid:
            yield row

    def each_cell(self):
        """
        Iterator over all cells in the grid
        """
        for row in self.each_row():
            for cell in row:
                yield cell

    def configure_cells(self):
        for cell in self.each_cell():
            row, col = cell.row, cell.column
            cell.cellNorth = self[row-1, col]
            cell.cellSouth = self[row+1, col]
            cell.cellWest = self[row, col-1]
            cell.cellEast = self[row, col+1]

    def random_cell(self):
        """
        Get a random cell from the grid
        """
        row = random.randint(0, self.rows-1)
        col = random.randint(0, self.columns-1)
        return self[row, col]

    def __getitem__(self, pos):
        row, col = pos
        if self.rows-1 >= row >= 0 and self.columns-1 >= col >= 0:
            return self.grid[row][col]
        return None

    def __str__(self):
        s = ""
        for row in range(self.rows):
            L = []
            for col in range(self.columns):
                L.append(str(self.grid[row][col]))
            s = s + ' '.join(L) + '\n'
        return s

if __name__ == "__main__":
    print Grid(10, 10)
    for row in Grid(4,4).prepare_grid():
        print row

    for cell in Grid(4,4).each_cell():
        print cell

    print
    g = Grid(4, 4)
    print g
    print g[1,2]
    print "Neighbors of g[1,2]"
    for cell in g[1,2].neighbors():
        print cell
    print "Neighbors of g[3,3]"
    for cell in g[3,3].neighbors():
        print cell

    print "A random cell"
    print g.random_cell()
    

