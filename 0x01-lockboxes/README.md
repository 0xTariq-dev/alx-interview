# LockBoxes Interview Preparation

## Description
In this Interview, we are tasked to write a method that determines if all the boxes can be opened.
the first box is always unlocked, and every box after has a set of keys that can unlock other boxes.
The method will return True if all boxes can be opened, else False.
The method will take a list of lists of integers as input.

## Example
The input data will be a list of lists of integers.
> input: 
```
boxes = [[1], [2], [3], [4], []]
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
```
> Output:
```
True
True
False
```

## Requirements
- Python 3.6 or higher
