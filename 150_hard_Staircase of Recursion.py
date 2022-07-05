"""
Staircase of Recursion
Write a function that returns the number of ways a person can climb n stairs, where the person may only climb 1 or 2 steps at a time.

To illustrate, if n = 4 there are 5 ways to climb:

[1, 1, 1, 1]
[2, 1, 1]
[1, 2, 1]
[1, 1, 2]
[2, 2]
Examples
ways_to_climb(1) ➞ 1

ways_to_climb(2) ➞ 2

ways_to_climb(5) ➞ 8
Notes
A staircase of height 0 should return 1.
"""

# v2
def ways_to_climb(n):
	if n < 2:
		return 1
	return ways_to_climb(n-1) + ways_to_climb(n-2)


# v1
# def fib(n):
#
# 	if n <= 1:
# 		return 1
# 	return fib(n-1) + fib(n-2)
#
# def ways_to_climb(n):
#
# 	return fib(n)

print(ways_to_climb(0))
print(ways_to_climb(1))
print(ways_to_climb(2))
print(ways_to_climb(3))
print(ways_to_climb(4))
print(ways_to_climb(5))
print(ways_to_climb(6))

