#!/usr/bin/env python
"""
Maze generation using the Aldous-Broder algorithm

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

from grid            import Grid
from distance_grid   import DistanceGrid
import argparse
import random

class AldousBroder: 
    """ This algorithm picks up a random cell from the grid,
    makes it the starting point and then randomly starts moving to the next
    neighbor, and then the next and so on until all the cells are visited 
    """

    def __init__(self):
        pass

    @staticmethod
    def create(grid):
        """ Core logic of this method """
        cells        = [cell for cell in grid.each_cell()]
        nCells       = len(cells)
        idx          = random.randint(0, nCells-1)
        current_cell = cells[idx]
        del cells

        visited_cells = set()
        visited_cells.add(current_cell)

        while len(visited_cells) != nCells:
            # Make a list of all the neighbors, visited or unvisited, and
            # choose a neighbor at random
            neighbors   = [cell for cell in current_cell.neighbors()]
            neighbor    = random.choice(neighbors)

            # If the chosen neighbor is not visited then link the neighbor with
            # the current cell, mark it visited, and move to neighbor. If the
            # neighbor is already visited then simply move to that neighbor
            # *without linking with the current cell*. 
            if neighbor not in visited_cells:
                current_cell.link(neighbor)
                visited_cells.add(neighbor)
            current_cell = neighbor

# Unit tests for Aldous-Broder
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
        AldousBroder.create(g)
        g.compute_distances(g[0,0])
    else:
        g = Grid(nRows, nColumns)
        AldousBroder.create(g)

    print g
