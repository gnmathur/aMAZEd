"""
Maze generation using the Sidewinder algorithm

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

class SidewinderMaze:
    """
    """
    def __init__(self):
        pass
    
    @staticmethod
    def create(grid):
        """
        Create a maze using the Sidewinder algorithm.

        This algorithm is an improvement over the Binary tree method. Instead
        of deciding to link N or E each turn, we create a 'run' of cell in each
        row. We decide to end the probabilistically. At the end of the run we
        choose a cell from a cell randomly, and link this cell to its North
        neighbor. 

        This algorithm also generates perfect mazes. The bias here are -
        a. Unbroken corridor at the top, same as in Binary tree
        b. Passages from South to North as trivial
        """
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)
                at_east_boundary = (cell.cellEast == None)
                at_north_boundary = (cell.cellNorth == None)

                should_close_out = (at_east_boundary) or ((not at_north_boundary) and (random.randint(0, 3) == 0))
                if should_close_out:
                    idx = random.randint(0, len(run)-1)
                    member = run[idx]
                    if member.cellNorth is not None:
                        member.link(member.cellNorth)
                    del run[:]
                else:
                    cell.link(cell.cellEast)

if __name__ == "__main__":
    nRows = input("Enter number of rows: ")
    nColumns = input("Enter number of columns: ")
    g = Grid(nRows, nColumns)
    SidewinderMaze.create(g)
    g.draw_ascii();
