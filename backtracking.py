#!/usr/bin/env python
"""
Maze generation using the backtracking method

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
from masked_grid import MaskedGrid
from mask import Mask
import argparse
from random import choice
from draw import MazeDraw

class Backtrack:
    """ Initialize the method
    """
    def __init__(self):
        pass

    @staticmethod
    def create(grid):
        """ Implementation for the backtracking method
        
        This method produces a grid with no bias. It does require auxilliary
        storage that is proportional to the size of the grid. Runtime
        complexity involves visiting each cell in the grid exactly twice.
        """
        def sample(lst):
            """ Helper routine to choose an element at random from a list """
            if len(lst) == 0:
                return None
            return choice(lst)
        
        # Main algorithm
        stack = []
        # Choose a starting cell at random
        current_cell = grid.random_cell()
        stack.append(current_cell)

        visited = set()
        visited.add(current_cell)
        
        while len(stack) > 0:
            # Choose an unvisited neighbor at random
            neighbors = [cell for cell in current_cell.neighbors() if cell not in visited]
            # If no unvisited neighbor then we are done with this current cell
            # and need to backtrack to the previously discivered cell
            if len(neighbors) == 0:
                current_cell = stack.pop()
            else:
                # Found an visited neighbor. Move to that cell and mark is
                # current. Also, link the current cell with the neighbor
                neighbor_cell = sample(neighbors)
                current_cell.link(neighbor_cell)
                visited.add(neighbor_cell)
                stack.append(neighbor_cell)
                current_cell = neighbor_cell

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-g", "--grid", action="store_true", help="Draw an ascii maze only")
    group.add_argument("-r", "--draw", action="store_true", help="Draw a maze image only")
    group.add_argument("-d", "--distance_grid", action="store_true", help="Draw a maze with distances from (0,0) marked")
    group.add_argument("-s", "--solution_grid", action="store_true", help="Draw a maze with solution")
    group.add_argument("-m", "--masked_grid", action="store_true", help="Draw a maze with solution")
    parser.add_argument("r", type=int, help="Number of rows")
    parser.add_argument("c", type=int, help="Number of columns")
    args = parser.parse_args()

    nRows = args.r
    nColumns = args.c
    if args.distance_grid:
        g = DistanceGrid(nRows, nColumns)
        Backtrack.create(g)
        g.compute_distances(g[0,0])
        print g
    elif args.solution_grid:
        g = SolutionGrid(nRows, nColumns)
        Backtrack.create(g)
        g.solve(g[0,0], g[nRows-1, nColumns-1])
        print g
    elif args.grid:
        g = Grid(nRows, nColumns)
        Backtrack.create(g)
        print g
    elif args.masked_grid:
        # m = Mask(nRows, nColumns)
        # m[0, 0] = False
        # m[1, 1] = False
        # m[2, 2] = False
        # m[3, 3] = False
        # m = Mask.from_image('maze_text.png')
        m = Mask.from_image('circle.png')
        g = MaskedGrid(m)
        Backtrack.create(g)
        MazeDraw(g, "BT").draw()
    elif args.draw:
        g = SolutionGrid(nRows, nColumns)
        Backtrack.create(g)
        g.solve(g[0,0], g[nRows-1, nColumns-1])
        MazeDraw(g, "Backtracking Method").draw()

