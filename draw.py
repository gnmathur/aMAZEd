#!/usr/bin/env python
"""
Draw an image of the maze on the screen

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

import pygame
import sys
from pygame.locals import *
from grid import Grid

COLOR_RAVEN = (102, 116, 128)
COLOR_SEPIA = (245, 223, 201)

class MazeDraw:
    def __init__(self, grid, title):
        self.nRows, self.nColumns = grid.dimensions()
        self.CW = 20
        self.CH = 20
        self.XMARGIN = 20
        self.YMARGIN = 20
        self.WW = self.CW * self.nColumns + self.XMARGIN
        self.WH = self.CH * self.nRows + self.YMARGIN
        self.grid = grid
        self.title = title

    def draw(self):

        pygame.init()
        BIT_COLOR_32 = 32
        SURFACE = pygame.display.set_mode((self.WW, self.WH), pygame.RESIZABLE, BIT_COLOR_32)
        pygame.display.set_caption(self.title)

        SURFACE.fill(COLOR_SEPIA)
        yoff = self.YMARGIN/2 # x offset
        for row in self.grid.each_row():
            xoff = self.XMARGIN/2 # y offset
            for cell in row:
                if not cell.isLinked(cell.cellNorth):
                    pygame.draw.line(SURFACE, COLOR_RAVEN, (xoff, yoff), (xoff+self.CW, yoff), 4)
                if not cell.isLinked(cell.cellSouth):
                    pygame.draw.line(SURFACE, COLOR_RAVEN, (xoff, yoff+self.CH), (xoff+self.CW, yoff+self.CH), 4)
                if not cell.isLinked(cell.cellWest):
                    pygame.draw.line(SURFACE, COLOR_RAVEN, (xoff, yoff), (xoff, yoff+self.CH), 4)
                if not cell.isLinked(cell.cellEast):
                    pygame.draw.line(SURFACE, COLOR_RAVEN, (xoff+self.CW, yoff), (xoff+self.CW, yoff+self.CH), 4)
                xoff = xoff + self.CW
            yoff = yoff + self.CH


        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

if __name__ == "__main__":
        g = Grid(10, 10)
        MazeDraw(g).draw()
