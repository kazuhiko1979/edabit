"""
Through the Grid
How many ways are there to navigate through a grid (w * h)?

Grid

Suppose you're on a 4 × 6 grid, and want to go from the bottom left to the top right. How many different paths can you take? Avoid backtracking, you can only move right or up.

Create a function that takes width and height and returns the amount of possibilities.

Examples
grid_pos([1, 1]) ➞ 2

grid_pos([6, 4]) ➞ 210

grid_pos([5, 5]) ➞ 252
"""
from scipy.special import perm

def grid_pos(lst):

    rights = lst[0]
    ups = lst[1]

    total = rights + ups

    #
    # pos = 1
    # for i in range(total, rights, -1):
    #     pos *= i
    #
    # redun = 1
    # for j in range(ups, 1, -1):
    #     redun *= j
    #
    # return pos / redun

    return perm(total, ups) / perm(ups, ups)

print(grid_pos([6, 4]))