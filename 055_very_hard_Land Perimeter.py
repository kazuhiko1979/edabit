"""
Land Perimeter
The function is given a map with 1 representing land, 0 representing water. A land cell can have four neighbors along its edges. Compute the total perimeter of shore-lines that are defined by land cells touching water or the outer edges of the map. Each cell edge has a length equal to 1. An isolated cell without neighbors has a total perimeter length of 4.

Examples
islands_perimeter([
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]) ➞ 16
islands_perimeter([
  [1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1],
]), 42)
islands_perimeter([
  [1, 0]
]) ➞ 4
"""
# v2
def islands_perimeter(grid):

	grid = [[0]+row+[0] for row in grid]
	grid = [[0]*len(grid[0])] + grid + [[0]*len(grid[0])]
	# print(grid)

	return sum(abs(grid[i][j] - grid[i-1][j]) + abs(grid[i][j]-grid[i][j-1]) for i in range(1,len(grid)) for j in range(1,len(grid[0])))

# v1
# def islands_perimeter(grid):
#
# 	rows, cols = len(grid), len(grid[0])
# 	land = set()
# 	for r in range(rows):
# 		for c in range(cols):
# 			if grid[r][c]:
# 				land.add((r, c))
#
# 	perimeter = 0
#
# 	for r, c in land:
# 		neighbors = 0
# 		for i, j in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
# 			if (r + i, c + j) in land:
# 				neighbors += 1
#
# 		perimeter += 4 - neighbors
#
# 	return perimeter

print(islands_perimeter([
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]))

print(islands_perimeter([
  [1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1],
]))
#
# print(islands_perimeter([
#   [1, 0]
# ]))
#
# print(islands_perimeter([
#     [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
#     [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
#     [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
#     [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
#     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
#     [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# ]))