"""
Sudoku Validation
Write a sudoku validator. This function should return True if the 2-D array represents a valid sudoku and False otherwise. To be a valid sudoku:

Each row must have the digits from 1 to 9 exactly once.
Each column must have the digits from 1 to 9 exactly once.
Each 3x3 box must have the digits from 1 to 9 exactly once.
Examples
sudoku_validator([
  [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]) ➞ True

sudoku_validator([
  [ 1, 1, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]) ➞ False
"""

def sudoku_validator(x):

    # リスト内、数字のユニークチェック
    def is_unique(nums):
        seen = set()
        for num in nums:
            if num != 0 and num in seen:
                return False
            seen.add(num)
        return True

    # 行列チェック
    for i in range(9):
        if not is_unique(x[i]) or not is_unique([x[j][i] for j in range(9)]):
            return False

    # 3x3 boxes チェック
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [x[z][y] for z in range(i, i + 3) for y in range(j, j + 3)]
            if not is_unique(box):
                return False

    return True


# import itertools
# import numpy as np
#
# def sudoku_validator(x):
#
#     one = []
#     two = []
#     three = []
#
#     sudoku_cross = list(itertools.chain.from_iterable(x))
#     count = 1
#
#     for i, n in enumerate(sudoku_cross, start=1):
#         if 1 <= count <= 3:
#             one.append(n)
#             count += 1
#             continue
#         if 4 <= count <= 6:
#             two.append(n)
#             count +=1
#             continue
#         if 7 <= count <= 9:
#             three.append(n)
#             count += 1
#             continue
#         if count == 10:
#             count = 2
#             one.append(n)
#             continue
#
#     x_t = np.array(x).T.tolist()
#
#     sudoku_crosses = [one, two, three]
#
#     for sudoku_cross in sudoku_crosses:
#         for i in range(0, len(sudoku_cross), 9):
#             x.append(sudoku_cross[i:i+9])
#
#     for t in x_t:
#         x.append(t)
#
#     result = [len(set(l)) == 9 for l in x]
#     return all(result)

print(sudoku_validator([
  [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))

print(sudoku_validator([
  [ 1, 1, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))

print(sudoku_validator(
[ [ 1, 3, 4, 6, 7, 8, 9, 1, 2 ],
  [ 6, 7, 2, 1, 9, 5, 3, 4, 8 ],
  [ 5, 9, 8, 3, 4, 2, 5, 6, 7 ],
  [ 8, 5, 9, 7, 6, 1, 4, 2, 3 ],
  [ 4, 2, 6, 8, 5, 3, 7, 9, 1 ],
  [ 7, 1, 3, 9, 2, 4, 8, 5, 6 ],
  [ 9, 6, 1, 5, 3, 7, 2, 8, 4 ],
  [ 2, 8, 7, 4, 1, 9, 6, 3, 5 ],
  [ 3, 4, 5, 2, 8, 6, 1, 7, 9 ] ]))

print(sudoku_validator([
  [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))

print(sudoku_validator([
  [ 1, 1, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))

print(sudoku_validator(
[ [ 1, 3, 4, 6, 7, 8, 9, 1, 2 ],
  [ 6, 7, 2, 1, 9, 5, 3, 4, 8 ],
  [ 5, 9, 8, 3, 4, 2, 5, 6, 7 ],
  [ 8, 5, 9, 7, 6, 1, 4, 2, 3 ],
  [ 4, 2, 6, 8, 5, 3, 7, 9, 1 ],
  [ 7, 1, 3, 9, 2, 4, 8, 5, 6 ],
  [ 9, 6, 1, 5, 3, 7, 2, 8, 4 ],
  [ 2, 8, 7, 4, 1, 9, 6, 3, 5 ],
  [ 3, 4, 5, 2, 8, 6, 1, 7, 9 ] ]))

print(sudoku_validator([
  [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))

print(sudoku_validator([
  [ 1, 1, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))

print(sudoku_validator(
[ [ 1, 3, 4, 6, 7, 8, 9, 1, 2 ],
  [ 6, 7, 2, 1, 9, 5, 3, 4, 8 ],
  [ 5, 9, 8, 3, 4, 2, 5, 6, 7 ],
  [ 8, 5, 9, 7, 6, 1, 4, 2, 3 ],
  [ 4, 2, 6, 8, 5, 3, 7, 9, 1 ],
  [ 7, 1, 3, 9, 2, 4, 8, 5, 6 ],
  [ 9, 6, 1, 5, 3, 7, 2, 8, 4 ],
  [ 2, 8, 7, 4, 1, 9, 6, 3, 5 ],
  [ 3, 4, 5, 2, 8, 6, 1, 7, 9 ] ]))

print(sudoku_validator(
[ [ 2, 5, 1, 4, 6, 9, 3, 7, 8 ],
  [ 7, 8, 9, 2, 1, 3, 4, 5, 6 ],
  [ 4, 3, 6, 5, 8, 7, 2, 9, 1 ],
  [ 6, 1, 3, 8, 7, 2, 5, 4, 9 ],
  [ 9, 7, 4, 1, 5, 6, 8, 2, 3 ],
  [ 8, 2, 5, 9, 3, 4, 1, 6, 7 ],
  [ 5, 6, 7, 3, 4, 8, 9, 1, 2 ],
  [ 2, 4, 8, 6, 9, 1, 7, 3, 5 ],
  [ 3, 9, 1, 7, 2, 5, 6, 8, 4 ] ]))





