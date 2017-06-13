#!/usr/bin/env python
"""
Class to help masking specific grid cells

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

from random import randint

class Mask:
    def __init__(self, n_rows, n_columns):
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.bits = [[True for _ in range(n_columns)] for _ in range(n_rows)]

    def __str__(self):
        return str(self.bits)

    def __getitem__(self, pos):
        """ Get a Boolean value from this mask for the specified position """
        row, column = pos
        if row <= self.n_rows-1 and column <= self.n_columns-1:
            return self.bits[row][column]
        else:
            return False
    def __setitem__(self, pos, is_on):
        """ Set a Boolean value in this Mask at specified position """
        row, column = pos
        self.bits[row][column] = is_on

    def count(self):
        """ Count the number of True values in this mask """
        return sum([self.bits[x][y] for x in range(self.n_rows)
                                    for y in range(self.n_columns)])

    def random_location(self):
        while True:
            row = randint(0, self.n_rows-1)
            col = randint(0, self.n_columns-1)
            if self.bits[row][col]:
                return self.bits[row][col]
    

if __name__ == "__main__":
    m = Mask(3, 4)
    for row in range(0, 3):
        for col in range(0, 4):
            m[row, col] = False
    m[1,2] = True
    print m
    print m.count()
    print m.random_location()
