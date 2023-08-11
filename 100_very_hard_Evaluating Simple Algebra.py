"""
Evaluating Simple Algebra
Given a string containing an algebraic equation, calculate and return the value of x. You'll only be given equations for simple addition and subtraction.

Examples
eval_algebra("2 + x = 19") ➞ 17

eval_algebra("4 - x = 1") ➞ 3

eval_algebra("23 + 1 = x") ➞ 24
Notes
There are spaces between every number and symbol in the string.
x may be a negative number.
"""

def eval_algebra(eq):
    eq = eq.split()
    if eq[4] == 'x':
        if eq[1] == '+':
            return int(eq[0]) + int(eq[2])
        else:
            return int(eq[0]) - int(eq[2])
    if eq[0] == 'x':
        if eq[1] == '+':
            return int(eq[4]) - int(eq[2])
        else:
            return int(eq[4]) + int(eq[2])
    if eq[2] == 'x':
        if eq[1] == '+':
            return int(eq[4]) - int(eq[0])
        else:
            return int(eq[0]) - int(eq[4])

# def eval_algebra(eq):
#
# 	eq = eq.split(' ')
#
# 	if eq[-1] == 'x':
# 		return eval(''.join(eq[:-2]))
#
# 	if eq[0] == 'x':
# 		if int(eq[2]) >= int(eq[-1]):
# 			if eq[1] == '+':
# 				return eval(''.join(eq[-1] + '-' + eq[2]))
# 			if eq[1] == '-':
# 				return eval(''.join(eq[-1] + '+' + eq[2]))
# 		elif int(eq[2]) <= int(eq[-1]):
# 			if eq[1] == '-':
# 				return eval(''.join(eq[-1] + '+' + eq[2]))
# 			if eq[1] == '+':
# 				return eval(''.join(eq[-1] + '-' + eq[2]))
#
# 	if eq[2] == 'x':
# 		if int(eq[0]) >= int(eq[-1]):
# 			if eq[1] == '+':
# 				return -(eval(''.join('-' + eq[-1] + '+' + eq[0])))
# 			if eq[1] == '-':
# 				return eval(''.join('-' + eq[-1] + '+' + eq[0]))
# 		elif int(eq[0]) <= int(eq[-1]):
# 			if eq[1] == '-':
# 				return eval(''.join(eq[-1] + '+' + eq[0]))
# 			if eq[1] == '+':
# 				return eval(''.join(eq[-1] + '-' + eq[0]))

print(eval_algebra("2 + x = 19"))
print(eval_algebra("4 - x = 1"))
print(eval_algebra("23 + 1 = x"))
print(eval_algebra("25 - 1 = x"))
print(eval_algebra("x + 10 = 53"))
print(eval_algebra("-23 + x = -20"))
print(eval_algebra("10 + x = 5"))
print(eval_algebra("-49 - x = -180"))
print(eval_algebra("x + 118 = 151"))
print(eval_algebra("x - 46 = -2"))
print(eval_algebra("-29 - x = -170"))
