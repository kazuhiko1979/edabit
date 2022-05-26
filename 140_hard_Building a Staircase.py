"""
Building a Staircase
Create a function that builds a staircase given the height and the type of building block.

Examples
build_staircase(3, "#") ➞ [
  ["#", "_", "_"],
  ["#", "#", "_"],
  ["#", "#", "#"]
]

build_staircase(4, "#") ➞ [
  ["#", "_", "_", "_"],
  ["#", "#", "_", "_"],
  ["#", "#", "#", "_"],
  ["#", "#", "#", "#"]
]

build_staircase(3, "A") ➞ [
  ["A", "_", "_"],
  ["A", "A", "_"],
  ["A", "A", "A"]
]

# height = 3 and building block = "A"

build_staircase(4, "$") ➞ [
  ["$", "_", "_", "_"],
  ["$", "$", "_", "_"],
  ["$", "$", "$", "_"],
  ["$", "$", "$", "$"]
]

# height = 4 and building block = "$"
Notes
If the height is 0, return an empty list [].
"""

def build_staircase(height, block):

	# v3
	return [[block]*i + ['_']*(height-i) for i in range(1, height+1)]


	# v2
	# arr = []
	# for i in range(1, height+1):
	# 	arr.append(list(block*i + '_'*(height-i)))
	# return arr


	# v1
	# result = []
	# count = height
	#
	# for i in range(height):
	# 	for j in range(height):
	# 		if i+j == height-1:
	# 			result.append(list(block*(height-j) + "_" * (count-1)))
	# 			count -= 1
	# return result


print(build_staircase(3, "#"))
print(build_staircase(4, "#"))
print(build_staircase(4, "$"))

