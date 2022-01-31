"""
Mini Sudoku
A Sudoku is a 9x9 grid that is completed when every 3x3 square, row and column consist of the numbers 1-9.

For this task, you will be given a completed 3x3 square, in the form of a two-dimensional list. Create a function that checks to make sure this 3x3 square contains each number from 1-9 exactly once. Make sure there are no duplicates, and no numbers outside this range.

Examples
is_mini_sudoku([[1, 3, 2], [9, 7, 8], [4, 5, 6]]) ➞ True

is_mini_sudoku([[1, 1, 3], [6, 5, 4], [8, 7, 9]]) ➞ False
# The 1 is repeated twice

is_mini_sudoku([[0, 1, 2], [6, 4, 5], [9, 8, 7]]) ➞ False
# The 0 is included (outside range)

"""

def is_mini_sudoku(square):

    return sorted(sum(square, [])) == list(range(1, 10))

    # square = [i for x in square for i in x]
    # return sorted(square) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


    #
    # TOTAL = 45
    # result = []
    # for i in square:
    #     for j in i:
    #         result.append(j)
    # return sum(result) == TOTAL

print(is_mini_sudoku([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))
print(is_mini_sudoku([[1, 1, 3], [6, 5, 4], [8, 7, 9]]))
print(is_mini_sudoku(
[[0, 1, 2],
[6, 4, 5],
[9, 8, 7]]))

