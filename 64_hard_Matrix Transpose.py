"""
Matrix Transpose
Create a function that transposes a 2D matrix.

Examples
transpose_matrix([
  [1, 1, 1],
  [2, 2, 2],
  [3, 3, 3]
]) ➞ [
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3]
]

transpose_matrix([
  [5, 5],
  [6, 7],
  [9, 1]
]) ➞ [
  [5, 6, 9],
  [5, 7, 1]
]
"""
import numpy

def transpose_matrix(lst):

    # result = []
    #
    # for i in range(len(lst[0])):
    #     result.append([lst[j][i] for j in range(len(lst))])
    # return result

    # return [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]


    # return [list(row) for row in zip(*lst)]



    # return numpy.transpose(lst)

    # print(len(lst[0]))
        # print(len(lst))
        # print(len(lst[1]))
        # print(len(lst[2]))



print(transpose_matrix([
  [1, 1, 1],
  [2, 2, 2],
  [3, 3, 3]
]))

print(transpose_matrix([
  [5, 5],
  [6, 7],
  [9, 1]
]))

