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
from distance_grid import DistanceGrid
import random
import argparse

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
        of deciding to link N or E each turn, we create a "run" of cells in each
        row. We decide to end the run probabilistically (1/4 probability) each 
        turn. At the end of the run we choose a cell from a run of cells 
        randomly, and link this cell to its North neighbor. 

        This algorithm also generates "perfect" mazes. The bias'es here are -
        a. Unbroken corridor at the top, same as in Binary tree
        b. Passages from South to North are trivial
        """
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)
                # A run ends at the ends boundary
                at_east_boundary = (cell.cellEast == None)
                # You cannot link to anything North in the northern-most row
                at_north_boundary = (cell.cellNorth == None)

                # Stop a run if we have reached the east end of a row or,
                # close it probabilistically (25% probability) each iteration
                should_close_out = (at_east_boundary) or ((not at_north_boundary) and (random.randint(0, 3) == 0))
                if should_close_out:
                    # This run needs to be closed out, now choose a cell from the cells collected in this
                    # run probabilistically. Each cell has equal probability of being chosen
                    idx = random.randint(0, len(run)-1)
                    member = run[idx]
                    if member.cellNorth is not None:
                        member.link(member.cellNorth)
                    # Clear out the cells collected in the previus run. 
                    del run[:]
                else:
                    # By default every cell is linked to its eastern neighbor
                    cell.link(cell.cellEast)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--distance_grid", action="store_true")
    group.add_argument("-g", "--grid", action="store_true")
    parser.add_argument("r", type=int, help="Number of rows")
    parser.add_argument("c", type=int, help="Number of columns")
    args = parser.parse_args()

    nRows = args.r
    nColumns = args.c
    if args.distance_grid:
        g = DistanceGrid(nRows, nColumns)
    else:
        g = Grid(nRows, nColumns)

    SidewinderMaze.create(g)
    g.draw_ascii();
