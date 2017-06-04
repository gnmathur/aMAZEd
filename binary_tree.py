"""
Maze generation using the binary tree algorithm

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

from cell import Cell
from grid import Grid
import random

class BinaryTreeMaze:
    """
    Algorithm to implements a 'perfect' maze. It has two major biases:
    a. There is always a 'diagonal' path from the South-west starting point
        to the North-east end
    b. The north-most row and the East-mode columns are always an unbroken
        corridor
    """
    def __init__(self):
        pass

    @staticmethod
    def create(grid):
        for cell in grid.each_cell():
            neighbors = []
            if cell.cellNorth is not None:
                neighbors.append(cell.cellNorth)
            if cell.cellEast is not None:
                neighbors.append(cell.cellEast)
            if len(neighbors):
                index = random.randint(0, len(neighbors)-1)
                neighbor = neighbors[index]
                cell.link(neighbor)

if __name__ == "__main__":
    nRows = input("Enter number of rows: ")
    nColumns = input("Enter number of columns: ")
    g = Grid(nRows, nColumns)
    BinaryTreeMaze.create(g)
    print g
