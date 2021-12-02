"""
Write a method that accepts two integer parameters rows and cols. The output is a 2d array of numbers displayed in column-major order, meaning the numbers shown increase sequentially down each column and wrap to the top of the next column to the right once the bottom of the current column is reached.

Examples
printGrid(3, 6) ➞ [
  [1, 4, 7, 10, 13, 16],
  [2, 5, 8, 11, 14, 17],
  [3, 6, 9, 12, 15, 18]
]

printGrid(5, 3) ➞ [
  [1, 6, 11],
  [2, 7, 12],
  [3, 8, 13],
  [4, 9, 14],
  [5, 10, 15]
]

printGrid(4, 1) ➞ [
  [1],
  [2],
  [3],
  [4]
]
# """
# import numpy as np
#
# def printgrid(rows, cols):
#
#     maxIndex = rows * cols + 1
#
#     index = 1
#     res = []
#     sublist = []
#
#     while index < maxIndex:
#         if index % rows == 0:
#             sublist.append(index)
#             res.append(sublist)
#             sublist = []
#             index += 1
#         else:
#             sublist.append(index)
#             index += 1
#
#     dic_t = np.array(res).T.tolist()
#     return dic_t


# def printgrid(rows, cols):
#     res = [[] for _ in range(rows)]
#     r = 0
#
#     for i in range(1, rows * cols + 1):
#         res[r].append(i)
#         if r == rows - 1:
#             r = 0
#         else:
#             r += 1
#     return res


def printgrid(rows, cols):

    return [[c*rows+r for c in range(cols)] for r in range(1, rows+1)]

print(printgrid(3, 6))
print(printgrid(5, 3))
print(printgrid(4, 1))
print(printgrid(1, 3))
print(printgrid(10, 2))

