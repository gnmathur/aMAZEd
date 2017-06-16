#!/usr/bin/env python
"""
aMAZEd menu

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
import argparse
from grid import Grid
from distance_grid import DistanceGrid
from solution_grid import SolutionGrid

from binary_tree import BinaryTreeMaze
from sidewinder import SidewinderMaze
from backtracking import Backtrack

ALGO_BINARY = "binary"
ALGO_SIDEWINDER = "sidewinder"
ALGO_BACKTRACKING = "backtracking"

if __name__ == "__main__":

    algo_cb = {
        ALGO_BINARY: BinaryTreeMaze.create,
        ALGO_SIDEWINDER: SidewinderMaze.create,
        ALGO_BACKTRACKING: Backtrack.create
    }

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(title='Rendering method', dest='subparser_name')
    parser.add_argument("--algo", default='binary', choices = [
        'binary', 'sidewinder', 'wilson', 'aldous-broder', 'backtracking'])

    dg_parser = subparser.add_parser('grid', help="Draw an ascii maze")
    dg_parser = dg_parser.add_argument_group()
    dg_parser.add_argument('r', type=int, help="Number of rows")
    dg_parser.add_argument('c', type=int, help="Number of columns")

    distg_parser = subparser.add_parser('distance-grid', help="Draw an ascii maze with distances from a given cell")
    distg_parser.add_argument('r', type=int, help="Number of rows")
    distg_parser.add_argument('c', type=int, help="Number of columns")
    distg_parser.add_argument('R', type=int, help="Row number of cell to start computing distances from")
    distg_parser.add_argument('C', type=int, help="Column number of cell to start computing distances from")

    sol_parser = subparser.add_parser('solution-grid', help="Draw an ascii maze with a path solution between two cells")
    sol_parser.add_argument('r', type=int, help="Number of rows")
    sol_parser.add_argument('c', type=int, help="Number of columns")
    sol_parser.add_argument('sr', type=int, help="Row number of cell to start solution path from")
    sol_parser.add_argument('sc', type=int, help="Columns number of cell to start solution path from")
    sol_parser.add_argument('er', type=int, help="Row number of cell to end solution path at")
    sol_parser.add_argument('ec', type=int, help="Column number of cell to end solution path at")

    img_parser = subparser.add_parser('image', help="Create an image of the maze")
    img_rc_group = img_parser.add_argument_group()
    img_rc_group.add_argument('r', type=int, help="Number of rows")
    img_rc_group.add_argument('c', type=int, help="Number of columns")
    img_solu_group = img_parser.add_argument_group()
    img_solu_group.add_argument('-sR', type=int, help="Row number of cell to start computing distances from")
    img_solu_group.add_argument('-sC', type=int, help="Column number of cell to start computing distances from")

    args = parser.parse_args()
    print args

    if args.subparser_name == "grid":
        g = Grid(args.r, args.c)
        algo_cb[args.algo](g)
        print g
    elif args.subparser_name == "distance-grid":
        g = DistanceGrid(args.r, args.c)
        algo_cb[args.algo](g)
        g.compute_distances(g[args.R, args.C])
        print g
    elif args.subparser_name == "solution-grid":
        g = SolutionGrid(args.r, args.c)
        algo_cb[args.algo](g)
        g.solve(g[args.sr, args.sc], g[args.er, args.ec])
        print g



