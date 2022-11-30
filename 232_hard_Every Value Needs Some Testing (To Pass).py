"""
Every Value Needs Some Testing (To Pass)
In this challenge, you have to verify that every, or some, of the given variables, pass a given test condition. There are seven parameters:

test: A string being the condition to verify.
val: A string with two possible values:
everybody if every variable has to pass the test;
somebody if at least one of the variables has to pass the test.
a, b, c, d, e: The variables being integers or booleans.
Create a function that returns True or False, depending on the result of the test applied to the variables.

Examples
every_some(">= 1", "everybody", 1, 1, -1, 1, 1) ➞ False
# Is every variable >= 1?

every_some(">= 1", "somebody", -1, -1, -1, -1, 1) ➞ True
# Is some variable >= 1?

every_some("< 4 / 2", "everybody", 1, 2, 1, 0, -10) ➞ False
# Is every variable < 2?
"""
# V3
def every_some(test, val, a, b, c, d, e):

	candidates = list(map(str, [a, b, c, d, e]))
	return (all if val == "everybody" else any)(eval(str(i) + test) for i in candidates)

# V2
# def every_some(test, val, a, b, c, d, e):
#
# 	candidates = list(map(str, [a, b, c, d, e]))
# 	if val == "everybody":
# 		return all([eval(i + test) for i in candidates])
# 	else:
# 		return any([eval(i + test) for i in candidates])

# v2
# def every_some(test, val, a, b, c, d, e):
#
# 	result = []
#
# 	for i in [a, b, c, d, e]:
#
# 		if eval(str(i) + test):
# 			result.append(True)
# 		else:
# 			result.append(False)
#
# 	if val == "everybody":
# 		if set(result) == {False}:
# 			return False
# 		if all(result) or not any(result):
# 			return True
# 		else:
# 			return False
# 	if val == "somebody":
# 		return len(set(result)) == 2


print(every_some(">= 1", "everybody", 1, 1, -1, 1, 1))
print(every_some(">= 1", "somebody", -1, -1, -1, -1, 1))
print(every_some("< 4 / 2", "everybody", 1, 2, 1, 0, -10))
print(every_some("!= 0", "everybody", False, False, False, False, False))
print(every_some("<= 10 * 2", "somebody", 21, 68, 104, 20, 3))
print(every_some("!= 1", "everybody", True, True, True, True, True))
print(every_some("== 9 % 9", "somebody", 9, 1, 81, 218, 33))