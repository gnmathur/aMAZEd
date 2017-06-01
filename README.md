# aMAZEd

Implementation of Maze algorithms

Python implementation of the algorithms presented in the book [Mazes for Programmers][REF1] by Jamis Buck

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

$ python sidewinder.py -d 6 8
+---+---+---+---+---+---+---+---+
|  2   1   2   3   4   5   6   7|
+---+---+---+---+---+---+---+   +
| 15  14  13  12  11  10   9   8|
+---+   +---+   +   +---+---+---+
| 16  15| 14  13| 12  13  14  15|
+   +---+---+---+---+---+   +   +
| 17  18| 19  18  17  16  15| 16|
+---+   +   +---+---+---+---+   +
| 20  19| 20| 21  20  19  18  17|
+   +---+---+---+---+   +   +---+
| 21  22  23  24  25| 20| 19  20|
+---+---+---+---+---+---+---+---+
```

License
----
MIT

[REF1]: https://www.amazon.com/Mazes-Programmers-Twisty-Little-Passages/dp/1680500554

