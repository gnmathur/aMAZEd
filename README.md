# aMAZEd

Implementation of various maze generation algorithms in python. 

#### Python package prequisites
* argparse
* random
* Pygame


## Binary Tree Method

```sh
$ python binary_tree.py
Enter number of rows: 8
Enter number of columns: 14
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|                                                       |
+   +   +---+---+   +   +---+   +   +   +---+---+   +   +
|   |   |           |   |       |   |   |           |   |
+   +   +---+   +   +   +---+---+---+---+---+---+---+   +
|   |   |       |   |   |                               |
+---+---+---+---+---+   +---+   +   +   +---+---+   +   +
|                       |       |   |   |           |   |
+---+---+---+   +---+---+---+   +   +---+   +---+   +   +
|               |               |   |       |       |   |
+---+   +---+   +---+---+---+---+   +---+---+   +   +   +
|       |       |                   |           |   |   |
+---+   +---+---+   +   +---+   +---+   +   +---+---+   +
|       |           |   |       |       |   |           |
+---+   +   +   +---+---+---+---+---+---+   +---+   +   +
|       |   |   |                           |       |   |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

```

> Source: [Mazes for Programmers][REF1] by Jamis Buck

## Sidewinder Algorithm


```sh
$ python sidewinder.py -h
usage: sidewinder.py [-h] [-d | -g] r c

positional arguments:
  r                    Number of rows
  c                    Number of columns

optional arguments:
  -h, --help           show this help message and exit
  -d, --distance_grid
  -g, --grid

$ python sidewinder.py -g 6 8
+---+---+---+---+---+---+---+---+
|                               |
+   +---+---+---+---+---+---+   +
|           |                   |
+---+---+   +   +   +---+   +---+
|           |   |   |           |
+---+---+---+   +---+   +---+   +
|                   |   |       |
+---+   +---+   +---+   +---+---+
|       |           |           |
+---+   +---+---+---+---+---+---+
|                               |
+---+---+---+---+---+---+---+---+

$ python sidewinder.py -d 6 12
+---+---+---+---+---+---+---+---+---+---+---+---+
|  0   1   2   3   4   5   6   7   8   9  10  11|
+---+---+   +   +---+   +   +   +---+   +---+---+
|  5   4   3|  4   5|  6|  7|  8| 11  10  11  12|
+   +---+   +---+---+---+---+---+---+---+---+---+
|  6|  5   4   5   6   7   8   9  10  11  12  13|
+---+---+   +---+---+---+---+---+---+---+---+   +
|  7   6   5   6   7   8   9  10| 17  16  15  14|
+---+---+---+   +   +---+---+   +---+   +   +   +
| 10   9   8   7|  8   9  10| 11| 18  17| 16| 15|
+---+   +---+   +---+   +---+---+---+   +   +---+
| 11  10  11|  8| 11  10| 21  20  19  18| 17  18|
+---+---+---+---+---+---+---+---+---+---+---+---+

```
> Source: [Mazes for Programmers][REF1] by Jamis Buck

## Aldous-broder Method

```sh
$ python aldous_broder.py -g 10 12
+---+---+---+---+---+---+---+---+---+---+---+---+
|                   |           |   |   |       |
+   +---+   +   +---+---+   +---+   +   +   +---+
|   |       |   |       |   |       |   |       |
+   +   +---+---+   +   +   +   +---+   +---+   +
|   |       |       |   |       |               |
+   +---+---+   +---+---+   +---+---+   +   +---+
|           |                   |       |       |
+---+   +   +   +---+   +   +   +   +---+---+   +
|       |   |       |   |   |           |   |   |
+---+---+   +   +   +   +   +   +---+---+   +   +
|   |           |   |   |   |   |               |
+   +   +---+---+---+   +---+---+   +   +   +---+
|   |   |       |               |   |   |       |
+   +---+---+   +---+---+   +---+---+   +---+   +
|                           |   |   |   |       |
+---+   +---+---+   +---+   +   +   +   +---+---+
|           |       |       |   |               |
+   +---+   +---+---+---+---+   +---+   +---+---+
|   |                           |               |
+---+---+---+---+---+---+---+---+---+---+---+---+
```

> Source: [Mazes for Programmers][REF1] by Jamis Buck

## Wilson's Algorithm

This algorithm takes longer than other methods to converge. The generated maze has no visible bias and a complex texture. 

```sh
$ python wilson.py -g 8 12
+---+---+---+---+---+---+---+---+---+---+---+---+
|   |                       |       |   |       |
+   +   +---+   +---+---+   +   +---+   +   +   +
|       |       |       |   |   |       |   |   |
+---+   +---+   +---+   +---+   +   +---+   +   +
|           |   |           |       |   |   |   |
+   +---+   +   +---+   +   +   +---+   +---+   +
|   |       |   |   |   |   |   |           |   |
+---+   +---+   +   +   +   +   +---+   +   +   +
|   |   |               |           |   |       |
+   +---+---+---+   +---+   +---+---+---+   +---+
|           |   |       |                   |   |
+---+---+   +   +---+   +---+   +   +   +   +   +
|   |                       |   |   |   |   |   |
+   +   +---+---+---+---+---+   +   +---+---+   +
|                   |           |               |
+---+---+---+---+---+---+---+---+---+---+---+---+

```
> Source: [Mazes for Programmers][REF1] by Jamis Buck

## Backtracking Method

Observationally this method generates mazes with the most complex texture. There are no biases the generated mazes.

```
$ python backtracking.py -h
usage: backtracking.py [-h] [-g | -r | -d | -s] r c

positional arguments:
  r                    Number of rows
  c                    Number of columns

optional arguments:
  -h, --help           show this help message and exit
  -g, --grid           Draw an ascii maze only
  -r, --draw           Draw a maze image only
  -d, --distance_grid  Draw a maze with distances from (0,0) marked
  -s, --solution_grid  Draw a maze with solution
```

```sh
$ python backtracking.py -g 8 14
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|                       |               |               |
+   +   +---+---+---+   +---+   +   +   +   +   +---+   +
|   |           |   |       |   |   |   |   |   |       |
+   +---+---+   +   +---+   +---+   +   +---+   +   +---+
|   |       |   |                   |       |   |   |   |
+   +   +   +   +---+---+---+---+---+---+   +   +   +   +
|   |   |       |                       |   |   |       |
+---+   +---+---+   +---+---+---+---+   +   +   +---+   +
|       |           |               |   |       |   |   |
+   +   +---+---+---+   +   +---+---+   +---+---+   +   +
|   |   |               |   |           |               |
+   +---+   +---+---+---+   +   +---+---+   +---+---+---+
|       |   |           |       |   |       |           |
+   +   +   +   +---+---+---+---+   +   +---+---+---+   +
|   |       |                                           |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
```

```sh
$ python backtracking.py -s 10 12
+---+---+---+---+---+---+---+---+---+---+---+---+
|0      |4   5      |13  14     |18  19  20  21 |
+   +---+   +   +   +   +   +---+   +---+---+   +
|1   2   3  |6  |   |12 |15  16  17 |        22 |
+   +---+---+   +---+   +---+---+---+   +---+   +
|   |       |7  |10  11             |   |   |23 |
+   +   +   +   +   +---+---+---+---+   +   +   +
|       |   |8   9  |                   |25  24 |
+---+---+---+---+---+   +---+---+---+---+   +---+
|               |       |       |32  31 |26  27 |
+   +---+---+   +   +---+---+   +   +   +---+   +
|           |       |           |33 |30  29  28 |
+---+---+   +---+---+   +---+   +   +---+---+---+
|   |       |           |       |34 |   |       |
+   +   +---+   +---+   +   +---+   +   +   +   +
|   |       |   |       |       |35 |   |   |   |
+   +---+   +   +   +---+---+---+   +   +   +   +
|       |   |   |   |           |36 |       |   |
+   +---+---+   +   +   +---+   +   +---+---+   +
|               |           |    37  38  39  40 |
+---+---+---+---+---+---+---+---+---+---+---+---+
```

```sh
$ python backtracking.py -r 20 26

![Backtracking Method](/images/backtracking_example.png)

> Source: [Mazes for Programmers][REF1] by Jamis Buck

License
----
MIT

[REF1]: https://www.amazon.com/Mazes-Programmers-Twisty-Little-Passages/dp/1680500554

