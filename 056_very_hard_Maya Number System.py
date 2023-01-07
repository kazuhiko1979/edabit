"""
Maya Number System
Maya numeral system was vigesimal (base 20) and positional: units, tens, hundreds (and so on) were read as descendant progressive powers of 20, instead of 10 like we do with our decimal system. Some examples:

- 39 => (1 x 20¹) + (19 x 20º)
- 815 => (2 x 20²) + (0 x 20¹) + (15 x 20º)
- 16125 => (2 x 20³) + (0 x 20²) + (6 x 20¹) + (5 x 20º)
Every digit (as to say the number to be multiplied for the power of 20) was symbolized with a combination of pebbles (dots), woodsticks (lines) and shells (used for the number 0) following a base5 system. See the table below:

Mayan Numbers

You must implement a function that, given a non-negative integer, returns a list of strings, with each string representing the symbolized single digit.

Symbols to use are "@" for shells, "-" for lines and "o" for dots. Dots have to be placed before the lines.

Examples
# Be careful, spaces between symbols are placed only for better readability!
# Don't use spaces in returned strings.

maya_number(39) ➞ ["o", "o o o o - - -"]

maya_number(815) ➞ ["o o", "@", "- - -"]

maya_number(16125) ➞ ["o o", "@", "o -", "-"]
Notes
Check the Resources tab for more info on Maya numerals (and Maya arithmetic).
All given integers are valid, no exceptions to handle.
"""

def maya_number(n):

	result = []
	for d in base(20, n):
		result.append('o'*(d % 5) + '-' * (d // 5) or '@')
	return result


def base(b, n):
	lst = []
	while n > 0:
		lst = [n % b] + lst
		n //= b
	return lst or [0]


# def maya_number(dec):
#
# 	result = []
#
# 	maya = {0: "@",
# 			1: "o",
# 			2: "oo",
# 			3: "ooo",
# 			4: "oooo",
# 			5: "-",
# 			6: "o-",
# 			7: "oo-",
# 			8: "ooo-",
# 			9: "oooo-",
# 			10: "--",
# 			11: "o--",
# 			12: "oo--",
# 			13: "ooo--",
# 			14: "oooo--",
# 			15: "---",
# 			16: "o---",
# 			17: "oo---",
# 			18: "ooo---",
# 			19: "oooo---",
# 			}
#
# 	if dec == 0:
# 		return ["@"]
#
# 	while dec > 0:
# 		x = dec % 20
# 		dec = int(dec / 20)
# 		result.append(int(x))
#
# 	return list(reversed([maya[i] for i in result]))


print(maya_number(39))
print(maya_number(815))
print(maya_number(16125))
print(maya_number(0))
print(maya_number(1985))
print(maya_number(86420))
print(maya_number(12579))
print(maya_number(666))





