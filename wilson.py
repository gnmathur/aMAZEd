#!/usr/bin/env python
"""
Maze generation using Wilson's algorithm

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
from distance_grid import DistanceGrid
from solution_grid import SolutionGrid
import argparse
import random

class Wilson:
    """ Wilson's algorithm for generating mazes

    The algorithm performs a random walk on the grid to create passages. This
    algorithm has no bias. Since every iteration we are performing a random
    walk from a random starting cell, and also erasing any loops in the
    process, the algorithm can take a long time to converge to a solution.
    """
    def __init__(self):
        pass
    
    @staticmethod
    def create(grid):
        def sample(lst):
            """ Helper routine to choose an element at random from a list """
            if len(lst) == 0:
                return None
            idx = random.randint(0, len(lst)-1)
            return lst[idx]
        
        # Main implementation start here
        #

        # Create a database of unvisited cells. At this point this is all the cells in the grid
        unvisited = []
        for cell in grid.each_cell():
            unvisited.append(cell)
        
        # Choose a starting cell at random and mark it as visited
        first = sample(unvisited)
        unvisited.remove(first)

        # Do this till we have visited all the cells in the grid. Each
        # iteration we will first choose a random cell to start from in the
        # grid. We will then choose a random neighbor of that cell and add it
        # to run path. We then irandomly choose a neighbor of that neighbor and
        # add that to the run path and so on. We keep building a path this way
        # till we hit a visited cell. At that point we will link all the cells
        # that we have marked added to the run path.
        while len(unvisited) > 0:
            # Choose a cell from the unvisited cells at random and add it to the run path.
            cell = sample(unvisited)
            path = [cell]
            
            # Keep finding random neighbors till we hit a visited cell
            while cell in unvisited:
                neighbor_cell = sample(cell.neighbors())
                if neighbor_cell in path:
                    path = path[0:path.index(neighbor_cell)+1]
                else:
                    path.append(neighbor_cell)
                cell = neighbor_cell

            # Link all the cells we found in the run.
            prev = None
            for cell in path:
                if prev:
                    prev.link(cell)
                    unvisited.remove(prev)
                prev = cell

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--distance_grid", action="store_true", help="print distances from (0, 0)")
    group.add_argument("-s", "--solution_grid", action="store_true")
    group.add_argument("-g", "--grid", action="store_true")
    parser.add_argument("r", type=int, help="Number of rows")
    parser.add_argument("c", type=int, help="Number of columns")
    args = parser.parse_args()

    nRows = args.r
    nColumns = args.c
    if args.distance_grid:
        g = DistanceGrid(nRows, nColumns)
        Wilson.create(g)
        g.compute_distances(g[0,nColumns-1])
    elif args.solution_grid:
        g = SolutionGrid(nRows, nColumns)
        Wilson.create(g)
        g.solve(g[0,0], g[nRows-1, nColumns-1])
    else:
        g = Grid(nRows, nColumns)
        Wilson.create(g)

    print g
