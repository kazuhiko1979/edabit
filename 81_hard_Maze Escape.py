"""
Maze Escape
Given a two-dimensional list of maze and a list of directions. Your task is to follow the given directions.

If you can reach the endpoint before all your moves have gone, return "Finish".
If you hit any walls or go outside the maze border, return "Dead".
If you find yourself still in the maze after using all the moves, return "Lost".
The maze list will look like this:

maze = [
  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 2, 1]
]

# 0 = Safe place to walk
# 1 = Wall
# 2 = Start Point
# 3 = Finish Point
# N = North, E = East, W = West and S = South
See the below examples for a better understanding:

Examples
exit_maze(maze, ["N", "E", "E"]) ➞ "Dead"
# Hitting the wall should return "Dead".

exit_maze(maze, ["N", "N", "N", "E"]) ➞ "Lost"
# Couldn't reach the finish point.

exit_maze(maze, ["N", "W", "W", "W", "N", "N", "N", "N", "W", "W", "S", "S", "S", "S", "W", "W", "N", "N", "N", "N", "N", "N", "N"]) ➞ "Finish"

"""

maze = [
  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 2, 1]
]

def exit_maze(maze, directions):

	for i in maze:
		if 2 in i:
			r, c = maze.index(i), i.index(2)

	print(r, c)

	for i in directions:
		if i == 'N':
			r -= 1
		if i == 'S':
			r += 1
		if i == 'W':
			c -= 1
		if i == 'E':
			c += 1
		try:
			if maze[r][c] == 1:
				return 'Dead'
			if maze[r][c] == 3:
				return 'Finish'
		except:
			return 'Dead'

	return 'Lost'



# def exit_maze(maze, directions):
# 	i = 9
# 	j = 8
# 	for direction in directions:
# 		if direction == "N":
# 			i -= 1
# 		elif direction == "S":
# 			i += 1
# 		elif direction == "E":
# 			j += 1
# 		else:
# 			j -= 1
# 		if i < 0 or i > 9 or j < 0 or j > 9:
# 			return "Dead"
# 		elif maze[i][j] == 1:
# 			return "Dead"
# 		elif maze[i][j] == 3:
# 			return "Finish"
# 	return "Lost"





# def calc(start, end, direction, maze):
#
# 	dic_direction = {
# 		'N': -1,
# 		'E': 1,
# 		'W': -1,
# 		'S': 1
# 	}
#
# 	for i in direction:
#
# 		if i == 'N':
# 			start[0] += dic_direction[i]
# 			if start == list(end):
# 				return 'Finish'
# 			try:
# 				if maze[start[0]][start[1]] == 0:
# 					continue
# 				elif maze[start[0]][start[1]] == 1:
# 					return 'Dead'
# 				else:
# 					return 'Lost'
# 			except IndexError:
# 				return 'Dead'
#
# 		if i == 'E':
# 			start[1] += dic_direction[i]
# 			if start == list(end):
# 				return 'Finish'
# 			try:
# 				if maze[start[0]][start[1]] == 0:
# 					continue
# 				elif maze[start[0]][start[1]] == 1:
# 					return 'Dead'
# 				else:
# 					return 'Lost'
# 			except IndexError:
# 				return 'Dead'
#
# 		if i == 'W':
# 			start[1] += dic_direction[i]
# 			if start == list(end):
# 				return 'Finish'
# 			try:
# 				if maze[start[0]][start[1]] == 0:
# 					continue
# 				elif maze[start[0]][start[1]] == 1:
# 					return 'Dead'
# 				else:
# 					return 'Lost'
# 			except IndexError:
# 				return 'Dead'
#
# 		if i == 'S':
# 			start[0] += dic_direction[i]
# 			if start == list(end):
# 				return 'Finish'
# 			try:
# 				if maze[start[0]][start[1]] == 0:
# 					continue
# 				elif maze[start[0]][start[1]] == 1:
# 					return 'Dead'
# 				else:
# 					return 'Lost'
# 			except IndexError:
# 				return 'Dead'
#
#
# 	if start != end:
# 		return "Lost"
#
# def find_index(maze, start_num, end_num, direction):
#
# 	# find start_index
# 	for start_row, i in enumerate(maze):
# 		try:
# 			start_column = i.index(start_num)
# 		except ValueError:
# 			continue
# 		start_index = start_row, start_column
# 		start_index = list(start_index)
#
# 	for end_row, j in enumerate(maze):
# 		try:
# 			end_column = j.index(end_num)
# 		except ValueError:
# 			continue
# 		end_index = end_row, end_column
# 		end_index = list(end_index)
#
#
# 	return calc(start_index, end_index, direction, maze)
#
#
# def exit_maze(maze, direction):
#
# 	return find_index(maze, 2, 3, direction)

print(exit_maze(maze,["N","N","N","W","W","W","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N"]))
print(exit_maze(maze,["N","N","N","N","N","N","N","N","W","W","W","S","W","W","N"]))
print(exit_maze(maze,["N","N","N","N","N","E","E","S","S","S","S","S","S"]))
print(exit_maze(maze,["N","W","W","W","W"]))
print(exit_maze(maze,["N","N","N","N","N","N","N","N","N","S","S","S","S","S","S","S","S","S"]))
print(exit_maze(maze,["N","E","E"]))
print(exit_maze(maze,["N","W","W","W","N","N","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N","S","S"]))
print(exit_maze(maze,["N","W","W","W","N","N"]))
print(exit_maze(maze,["N","N","N","E"]))
print(exit_maze(maze,["N","N","N","W","W","W","N","N","W","W","S","S","S","S","S","S"]))
print(exit_maze(maze,["N","W","W","W","N","N","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N"]))