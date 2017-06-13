#!/usr/bin/env python
"""
A masked grid

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
from mask import Mask
from cell import Cell

class MaskedGrid(Grid):
    def __init__(self, mask):
        self.mask = mask
        super(MaskedGrid, self).__init__(mask.n_rows, mask.n_columns)

    # Overriden method from Grid class
    def prepare_grid(self):
        grid = [[Cell(row, col) if self.mask[row, col] else None for col in range(self.columns)] for row in range(self.rows)]
        return grid
                                                                
if __name__ == "__main__":
    mask = Mask(3,4)
    mask[2, 3] = False
    mask[0, 2] = False
    mg = MaskedGrid(mask)
