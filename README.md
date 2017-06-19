# aMAZEd

Implementation of various maze generation algorithms in python. 

> Source: [Mazes for Programmers][REF1] by Jamis Buck

#### Python package prequisites
* argparse
* random
* Pygame

## Usage

```sh

$ python amazed.py --help
usage: amazed.py [-h]
                 [--algo {binary,sidewinder,wilson,aldous-broder,backtracking}]
                 {grid,distance-grid,solution-grid,image,masked-image} ...

optional arguments:
  -h, --help            show this help message and exit
  --algo {binary,sidewinder,wilson,aldous-broder,backtracking}

Rendering method:
  {grid,distance-grid,solution-grid,image,masked-image}
    grid                Draw an ascii maze
    distance-grid       Draw an ascii maze with distances from a given cell
    solution-grid       Draw an ascii maze with a path solution between two
                        cells
    image               Draw an image of the maze
    masked-image        Draw an image of a maze where the maze is created from
                        a mask specified in a B&W image file
```

## Examples

### ASCII maze generation using the Binary method

```sh
$ python amazed.py --algo binary grid 8 8
+---+---+---+---+---+---+---+---+
|                               |
+---+---+   +---+   +---+---+   +
|           |       |           |
+---+---+   +---+---+   +---+   +
|           |           |       |
+   +   +---+---+   +---+   +   +
|   |   |           |       |   |
+   +   +---+   +---+---+---+   +
|   |   |       |               |
+---+---+---+   +---+   +---+   +
|               |       |       |
+   +   +---+   +   +   +   +   +
|   |   |       |   |   |   |   |
+   +   +   +---+   +---+   +   +
|   |   |   |       |       |   |
+---+---+---+---+---+---+---+---+
```

### ASCII maze generation and solution using Sidewinder method

```sh
$ python amazed.py --algo sidewinder solution-grid 10 20 9 0 0 19
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|                                25  26  27  28  29  30  31  32  33  34  35  36 |
+   +   +---+---+---+---+---+---+   +---+   +---+   +   +---+   +---+---+---+   +
|   |               |21  22  23  24 |           |   |   |           |           |
+   +---+---+---+---+   +---+---+---+---+   +---+---+---+   +---+---+---+---+---+
|       |            20  19  18  17  16 |       |                               |
+   +---+---+---+---+---+---+   +---+   +   +---+---+---+   +---+---+---+---+   +
|                           |   |14  15 |               |           |           |
+---+   +---+   +   +   +---+---+   +---+---+---+---+---+   +---+---+---+   +---+
|           |   |   |       |12  13     |                       |               |
+---+   +---+---+---+---+---+   +---+---+---+---+---+---+---+---+---+---+   +---+
|       |                10  11                                         |       |
+---+---+---+---+   +---+   +---+---+---+---+---+   +---+---+   +   +   +---+---+
|                   |8   9      |                           |   |   |           |
+   +---+---+---+---+   +---+---+   +---+   +---+---+---+---+---+---+---+---+   +
|   |3   4   5   6   7          |   |                           |               |
+---+   +   +---+---+   +---+---+---+   +---+---+---+---+---+   +---+   +---+---+
|    2  |   |                   |                           |       |           |
+---+   +---+---+---+   +---+---+   +---+   +---+   +---+---+---+---+   +---+   +
|0   1      |               |           |   |                   |           |   |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
```

### Maze image generation using Wilson's algorithm

```sh
$ python amazed.py --algo wilson image 15 15
```

![Wilson Method](/images/ex_wilson.png)

### Maze image generation using Backtracking method over a masked grid

```sh
$ python amazed.py --algo backtracking masked-image images/templates/circle.png
```

![Backtracking Method using a mask](/images/ex_backtracking_masked.png)


License
----
MIT

[REF1]: https://www.amazon.com/Mazes-Programmers-Twisty-Little-Passages/dp/1680500554

