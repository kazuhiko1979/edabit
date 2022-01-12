"""
Rotate a Matrix 90 Degrees Clockwise
Create a function that receives a square n*n matrix and returns that matrix after it has been rotated 90 degrees in the clockwise direction.

Examples
rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]

rotate([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]) ➞ [
  ["m", "i", "e", "a"],
  ["n", "j", "f", "b"],
  ["o", "k", "g", "c"],
  ["p", "l", "h", "d"]
]
"""

import numpy as np

def rotate(lst):

    # return [list(t) for t in zip(*reversed(lst))]

    # return np.rot90(np.array(lst), k=3).tolist()

    tpose = map(list, zip(*lst))
    return [i[::-1] for i in tpose]


    # lst = np.array(lst).T
    # return [i[::-1].tolist() for i in lst]




print(rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]])
)