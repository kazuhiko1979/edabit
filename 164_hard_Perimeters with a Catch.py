"""
Perimeters with a Catch
Write a function that takes a number and returns the perimeter of either a circle or a square. The input will be in the form (letter l, number num) where the letter will be either "s" for square, or "c" for circle, and the number will be the side of the square or the radius of the circle.

Use the following formulas:

Perimeter of a square: 4 * side.
Perimeter of a circle: 6.28 * radius.
The catch is you can only use arithmetic or comparison operators, which means:

No if... else statements.
No dictionaries.
No lambdas.
No formatting methods, etc.
The goal is to write a short, branch-free piece of code.

Examples
perimeter("s", 7) ➞ 28

perimeter("c", 4) ➞ 25.12

perimeter("c", 9) ➞ 56.52
Notes
No rounding is needed.
Hint: The Boolean True, used with arithmetic operators, counts as 1, while False counts as 0. That means (a>b)+1 will return 1 or 2, depending on the values of a and b.
"""

def perimeter(lt, num):

	# while lt == "s":
	# 	return 4 * num
	# while lt == "c":
	# 	return 6.28 * num

	# return [4 * num, 6.28 * num][lt == 'c']

	# return num * 4 if lt == "s" else num * 6.28

print(perimeter("s", 7))
print(perimeter("c", 4))
print(perimeter("c", 9))