"""
Clear Brackets
Create a function brackets() that takes a string and checks that the brackets in the math expression are correct. The function should return True or False.

Examples
brackets("(a*(b-c)..... )") ➞ True

brackets(")(a-b-45/7*(a-34))") ➞ False

brackets("sin(90...)+.............cos1)") ➞ False
Notes
The string may not contain brackets, then return True.
String may contain spaces.
The string may be empty.
"""
# v3
def brackets(exp):
	
	b = ''.join(b for b in exp if b in '()')
	return b.count('(') == b.count(')') and '(' not in b or b[0] == '(' and b[-1] == ')'


# v2
# def brackets(exp):
# 	count = 0
# 	for c in exp:
# 		if c == '(':
# 			count += 1
# 		elif c == ')':
# 			count -= 1
# 		if count < 0:
# 			return False
# 	return count == 0


# v1
# def brackets(exp):
#
# 	top_bracket = 0
# 	bottom_bracket = 0
#
# 	for i in exp:
# 		if i == ")":
# 			if top_bracket == 0:
# 				return False
# 			else:
# 				bottom_bracket += 1
# 		elif i == "(":
# 			top_bracket += 1
# 		elif i == ")":
# 			bottom_bracket += 1
#
# 		if top_bracket == bottom_bracket:
# 			top_bracket = 0
# 			bottom_bracket = 0
#
# 	return top_bracket == bottom_bracket


print(brackets("(a*(b-c)..... )"))
print(brackets(")(a-b-45/7*(a-34))"))
print(brackets("sin(90...)+.............cos1)"))
print(brackets(" (...). .%_.(.... )"))
print(brackets(" (...)...(..(...).... )  "))
print(brackets(") .. .() (        ).. . ("))
print(brackets(")))((("))
print(brackets("  (...).!.)...("))
print(brackets("a+b"))
print(brackets(""))
print(brackets("(a+f).`!=.)...) "))