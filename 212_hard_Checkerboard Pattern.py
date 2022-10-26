"""
Checkerboard Pattern
Create a function that returns True if the two-dimensional n x n input array has a checker-board pattern.

Examples
is_checkerboard([
  [1, 1],
  [0, 1]
]) ➞ False

is_checkerboard([
  [0, 1],
  [1, 0]
]) ➞ True

is_checkerboard([
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 1, 1]
]) ➞ False

is_checkerboard([
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1]
]) ➞ True
Notes
An element in the array adheres to the checker-board pattern if the elements directly to the left, right, top and below are of a different type, and the elements on the diagonal direction are of the same type.
The element in the upper-left corner can be either 0 or 1
"""
# v3
def is_checkerboard(lst):

    return sum(lst, []) == sum(lst, [])[::-1]


# v2
# def is_checkerboard(lst):
#
#     ul = lst[0][0]
#
#     even = [int(i % 2 != ul) for i in range(len(lst))]
#     odd = [int(i % 2 == ul) for i in range(len(lst))]
#
#     return all([row == [even, odd][i%2] for i, row in enumerate(lst)])


# v1
# from itertools import groupby
#
# def is_checkerboard(lst):
#
#     odd = []
#     even = []
#     even.append(lst[0])
#
#     for i in range(1, len(lst)):
#         if i % 2 == 0:
#             even.append(lst[i])
#         else:
#             odd.append(lst[i])
#
#     if len(even) == 1 and len(odd) == 1:
#         for e, o in zip(even, odd):
#             for i, j in zip(e, o):
#                 if i == j:
#                     return False
#
#     g_even = groupby(even)
#     g_odd = groupby(odd)
#
#     even_result = next(g_even, True) and not next(g_even, False)
#     odd_result = next(g_odd, True) and not next(g_odd, False)
#     return even_result == odd_result


#
print(is_checkerboard([
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 1, 1]
]))

print(is_checkerboard([
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1]
]))
#
print(is_checkerboard([
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 1, 1],
	[0, 1, 0, 1, 0]
]))
#
print(is_checkerboard([
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[1, 1, 0, 1, 0]
]))
#
print(is_checkerboard([
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 1, 1]
]))
#
print(is_checkerboard([
	[0, 1],
	[1, 0]
]))

print(is_checkerboard([
	[1, 1],
	[1, 0]
]))

print(is_checkerboard([
	[1, 0],
	[0, 1]
]))
#
print(is_checkerboard([
	[1, 0, 1],
	[0, 1, 0],
	[1, 0, 1]
]))