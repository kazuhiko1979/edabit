"""
Peeling off the Outer Layers
Given a list of lists, return a new list of lists containing every element, except for the outer elements.

Examples
peel_layer_off([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]) ➞ [
  ["f", "g"],
  ["j", "k"]
]

peel_layer_off([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35]
]) ➞ [
  [7, 8, 9],
  [12, 13, 14],
  [17, 18, 19],
  [22, 23, 24],
  [27, 28, 29]
]

peel_layer_off([
  [True, False, True],
  [False, False, True],
  [True, True, True]
]) ➞ [[False]]

peel_layer_off([
  ["hello", "world"],
  ["hello", "world"]
]) ➞ []
Notes
The 2D grid is always a rectangular/square shape.
Always return some form of nested list, unless there are no elements. In that case, return an empty list.
"""

def peel_layer_off(lst):

    return [i[1:-1] for i in lst[1:-1]]

    l = []
    for sub in lst[1:-1]:
        l.append(sub[1:-1])
    return l


    # bottom_num = len(lst) - 1
    # res = []
    # for i in range(0, len(lst)):
    #     if i == 0:
    #         continue
    #     elif i == bottom_num:
    #         continue
    #     else:
    #         res.append(lst[i][1:-1])
    # return res



print(peel_layer_off([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]))







