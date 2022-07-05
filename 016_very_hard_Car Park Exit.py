"""
Car Park Exit
You are stuck in a multi-storey car parking lot. Your task is to exit the carpark using only the staircases. Exit is always at the bottom right of the ground floor.

Create a function that takes a two-dimensional list where:

Free carparking spaces are represented by a 0
Staircases are represented by a 1
Your starting position is represented by a 2 and can be at any level of the car park.
Exit is always at the bottom right of the ground floor.
You must use the staircases (1) to go down a level.
Each floor will have only one staircase apart from the ground floor which will not have any staircases.
... and returns a list of the quickest route out of the carpark.

arr = [
  [1, 0, 0, 0, 2],
  [0, 0, 0, 0, 0]
]

# Starting from 2, move to left 4 times = "L4"
# Go down from stairs 1 step = "D1"
# Move to right 4 times to exit from right bottom corner = "R4"

result = ["L4", "D1", "R4"]
See the below examples to better understand:

Examples
parking_exit([
  [1, 0, 0, 0, 2],
  [0, 0, 0, 0, 0]
]) ➞ ["L4", "D1", "R4"]
parking_exit([
  [2, 0, 0, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0]
]) ➞ ["R3", "D2", "R1"]

# Starting from 2, move to right 3 times = "R3"
# Go down from stairs 2 steps = "D2"
# Move to right 1 step to exit from right bottom corner = "R1"
parking_exit([[0, 0, 0, 0, 2]]) ➞ []
# You are already at right bottom corner.
"""
def parking_exit(lst):

	ret = []
	if len(lst) == 1:
		return ret

	pos = lst[0].index(2)
	print(pos)
	lst[-1][-1] = 1
	print(lst)

	for i in lst:
		if i.index(1) < pos:
			ret.append('L' + str(pos-i.index(1)))
			pos = i.index(1)
			ret.append('D1')
		elif i.index(1) > pos:
			ret.append('R' + str(i.index(1)-pos))
			pos = i.index(1)
			ret.append('D1')
		elif i.index(1) == pos:
			ret[-1] = "D" + str(int(ret[-1][1:])+1)

	return ret[:-1] if ret[-1] == "D1" else ret[:-1] + ['D' + str(int(ret[-1][1:])-1)]






print(parking_exit([[1, 0, 0, 0, 2], [0, 0, 0, 0, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
# ["L4", "D1", "R4", "D1", "L4", "D1", "R4"]))

print(parking_exit([[1, 0, 0, 0, 2], [0, 0, 0, 0, 0]]))
# ["L4", "D1", "R4"]

print(parking_exit([[2, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]))
# ["R3", "D2", "R1"])