"""
Check if the Formula is Correct
Create a function that takes a string and returns True or False depending on whether or not the given formula is correct.

Examples
formula("6 * 4 = 24") ➞ True

formula("18 / 17 = 2") ➞ False

formula("") ➞ None
Notes
You have to figure out what a is.
Ignore the spaces.
If the input is an empty string "", return None.
You do not need to dynamically find the value of a (it's a constant and the same accross all tests).
"""

def formula(txt):

	# v3
	t = txt.replace('a', '4').replace('=', '==')
	return eval(t) if txt else None


	# v2
	# if txt == "":
	# 	return None
	# txt = txt.replace('a', '4')
	# lst = txt.split("=")
	# return len(set([eval(x) for x in lst])) == 1


	# v1
	# if txt == "":
	# 	return None
	#
	# txt = ''.join(txt.split())
	# answer = []
	# formura = ""
	#
	# for j, i in enumerate(txt.lstrip()):
	# 	if i == "a":
	# 		i = "4"
	# 	if i != "=":
	# 		formura += i
	# 	if i == "=":
	# 		answer.append(formura)
	# 		formura = ""
	# 	if j == len(txt) - 1:
	# 		answer.append(formura)
	#
	# return len(set(eval(i) for i in answer)) == 1


print(formula("6 * 4 = 24"))
print(formula('120 - 7 = 100'))
print(formula('16 - 8 = 16 / 2 = 64 / 8'))
print(formula('a = a'))
print(formula('a * 7 = 90'))
print(formula('16 * 10 = 160 = 14 + 120'))
print(formula('a = 4'))
print(formula(''))
print(formula('1000 / 10 = 100 = 2 * 50'))
print(formula('18 / 17 = 2'))
print(formula('(1+2+3+4+5+6+7+8)/a=9'))
print(formula('2 * 2 * 2 = a * 2 = 8'))
print(formula('   8/       9 =       5'))
print(formula('1111           /     101=     11'))
print(formula('a / a = a - 3'))
