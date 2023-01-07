"""
Simple Minesweeper
Given a 2D array of mines, replace the question mark with the number of mines that immediately surround it. This includes the diagonals, meaning it is possible for it to be surrounded by 8 mines maximum.

The key is as follows:

An empty space: "-"
A mine: "#"
Number showing number of mines surrounding it: "?"
Examples
minesweeper([
  ["-", "#", "-"],
  ["-", "?", "-"],
  ["-", "-", "-"]
]) ➞ [
  ["-", "#", "-"],
  ["-", "1", "-"],
  ["-", "-", "-"]
]

minesweeper([
  ["-", "#", "-"],
  ["#", "-", "?"],
  ["#", "#", "-"]
]) ➞ [
  ["-", "#", "-"],
  ["#", "-", "2"],
  ["#", "#", "-"]
]

minesweeper([
  ["-", "#", "#"],
  ["?", "#", ""],
  ["#", "?", "-"]
]) ➞ [
  ["-", "#", "#"],
  ["3", "#", ""],
  ["#", "2", "-"]
]

minesweeper([
  ["-", "-", "#"],
  ["?", "-", "-"],
  ["-", "-", "-"]
]) ➞ [
  ["-", "-", "#"],
  ["0", "-", "-"],
  ["-", "-", "-"]
]
Notes
You will only be given 3x3 grids.
The question mark is not limited to the centre (there may be multiple question marks).
"""
def minesweeper(grid):

	for i, m in enumerate(grid):
		for j, n in enumerate(m):
			if n == '?':
				ctr = 0
				for x in range(max(0, i-1), i+2):
					for y in range(max(0, j-1), j+2):
						try:
							if grid[x][y] == '#':
								ctr += 1
							else:
								ctr = 0
						except:
							pass
				grid[i][j] = str(ctr)
	return grid


# def minesweeper(grid):
#
# 	for i in range(0, len(grid)):
# 		grid[i].insert(0, '-')
# 		grid[i].append('-')
#
# 	grid.insert(0, ['-', '-', '-', '-', '-'])
# 	grid.append(['-', '-', '-', '-', '-'])
#
# 	count = 0
#
# 	for subarray in grid:
# 		for word in subarray:
# 			if '?' == word:
# 				mark_index = [grid.index(subarray), subarray.index('?')]
# 				start_index = mark_index[0]-1, mark_index[1]-1
# 				end_index = mark_index[0]+1, mark_index[1]+1
#
# 				for r in range(start_index[0], end_index[0]+1):
# 					for c in range(start_index[1], end_index[1]+1):
# 						if grid[r][c] == "#":
# 							count += 1
# 							if r > end_index[0]+1 and c > end_index[1]+1:
# 								continue
#
# 				grid[mark_index[0]][mark_index[1]] = str(count)
# 				count = 0
#
# 	return [grid[i][1:-1] for i in range(1, len(grid)-1)]


print(minesweeper([
  ["-", "#", "-"],
  ["-", "?", "-"],
  ["-", "-", "-"]
]))
#
print(minesweeper([
  ["-", "#", "-"],
  ["#", "-", "?"],
  ["#", "#", "-"]
]))
#
print(minesweeper([
  ["-", "#", "#"],
  ["?", "#", ""],
  ["#", "?", "-"]
]))

print(minesweeper([
  ["-", "-", "#"],
  ["?", "-", "-"],
  ["-", "-", "-"]
]))

print(minesweeper([
  ["?", "?", "?"],
  ["?", "#", "?"],
  ["?", "?", "?"]
]))


print(minesweeper([
  ["?", "?", "?"],
  ["?", "?", "?"],
  ["?", "?", "?"]
]))

print(minesweeper([
  ["#", "#", "#"],
  ["#", "-", "#"],
  ["#", "#", "#"]
]))