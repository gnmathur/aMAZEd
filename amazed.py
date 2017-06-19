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
import time
import datetime

from grid            import Grid
from distance_grid   import DistanceGrid
from solution_grid   import SolutionGrid
from draw            import MazeDraw
from mask            import Mask
from masked_grid     import MaskedGrid

from binary_tree     import BinaryTreeMaze
from sidewinder      import SidewinderMaze
from backtracking    import Backtrack
from aldous_broder   import AldousBroder
from wilson          import Wilson

ALGO_BINARY          = "binary"
ALGO_SIDEWINDER      = "sidewinder"
ALGO_BACKTRACKING    = "backtracking"
ALGO_ALDOUS_BRODER   = "aldous-broder"
ALGO_WILSON          = "wilson"

def timestamp():
    return str(datetime.datetime.now())

if __name__ == "__main__":

    algo_cb = {
        ALGO_BINARY:          BinaryTreeMaze.create,
        ALGO_SIDEWINDER:      SidewinderMaze.create,
        ALGO_BACKTRACKING:    Backtrack.create,
        ALGO_ALDOUS_BRODER:   AldousBroder.create,
        ALGO_WILSON:          Wilson.create
    }

    parser     = argparse.ArgumentParser()
    subparser  = parser.add_subparsers(title='Rendering method', dest='subparser_name')
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

    img_parser       = subparser.add_parser('image', help="Draw an image of the maze")
    img_rc_group     = img_parser.add_argument_group()
    img_rc_group.add_argument('r', type=int, help="Number of rows")
    img_rc_group.add_argument('c', type=int, help="Number of columns")

    mimg_parser       = subparser.add_parser('masked-image', help="Draw an image of a maze where the maze is created from a mask specified in a B&W image file")
    mimg_rc_group     = mimg_parser.add_argument_group()
    mimg_rc_group.add_argument('mask_img', type=file, help="Masked image")

    args = parser.parse_args()

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
    elif args.subparser_name == "masked-image":
        m = Mask.from_image(args.mask_img)
        g = MaskedGrid(m)
        Backtrack.create(g)
        MazeDraw(g, 'Maze '+timestamp()).draw()
    elif args.subparser_name == "image":
        g = Grid(args.r, args.c)
        Backtrack.create(g)
        MazeDraw(g, 'Maze '+timestamp()).draw()
