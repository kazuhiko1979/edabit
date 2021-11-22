"""
In the Centre?
Given a string containing mostly spaces and one non-space character, return whether the character is positioned in the very centre of the string. This means the number of spaces on both sides should be the same.

Examples
is_central("  #  ") ➞ True

is_central(" 2    ") ➞ False

is_central("@") ➞ True
Notes
Only one character other than spaces will be given at a time.
"""
import math

def is_central(txt):

	if len(txt) % 2 != 0:
		return True if txt[math.ceil(len(txt) / 2) - 1] != " " else False
	return False


print(is_central("  #  "))
print(is_central("@"))
print(is_central(' 2    '))
print(is_central(' 1'))
print(is_central('7 '))