"""
ABACABA Pattern
The ABACABA pattern is a recursive fractal pattern that shows up in many places in the real world (such as in geometry, art, music, poetry, number systems, literature and higher dimensions).

Create a function that takes a number n as an argument and returns a string that represents the full pattern.

Examples
abacaba_pattern(1) ➞ "A"

abacaba_pattern(2) ➞ "ABA"

abacaba_pattern(3) ➞ "ABACABA"
Notes
Result should always be uppercase.
"""
# v2
def abacaba_pattern(n):
	if n == 1:
		return 'A'
	wrap = abacaba_pattern(n-1)
	return wrap + chr(64 + n) + wrap



# v1
# alpha = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# def abacaba_pattern(num, count=1):
#
# 	if num == 1:
# 		return "A"
# 	if count < num:
# 		pattern = alpha[count]
# 		count += 1
# 		return make_pattern(num, count, pattern)
#
# def make_pattern(num, count, pattern):
# 	while count < num:
# 		pattern = pattern + alpha[count] + pattern
# 		count += 1
# 		return make_pattern(num, count, pattern)
# 	if count == num:
# 		pattern = pattern + alpha[count] + pattern
# 	return pattern


print(abacaba_pattern(1))
print(abacaba_pattern(2))
print(abacaba_pattern(3))
print(abacaba_pattern(4))
print(abacaba_pattern(5))



