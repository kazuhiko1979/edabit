"""
Complex Numbers
Write a function that takes a string "a + bi" and returns a tuple (a, b).

Examples
complex_to_tuple("1 + 2i") ➞ (1, 2)

complex_to_tuple("6 + 9i") ➞ (6, 9)

complex_to_tuple("-7 - 2i") ➞ (-7, -2)
Notes
All strings are going to have the (±)a ± bi format, (where a and b are integers).
"""
import re

def complex_to_tuple(param):

	# v3
	a, b = param[:-1].replace('+', ' +').replace('-', ' -').split()
	# print(a, b)
	return (eval(a), eval(b))


	# v2
	# if '+' in param:
	# 	plus = param.find('+')
	# 	num = int(param[:plus])
	# 	imaginary = int(param[plus+1:-1])
	#
	# 	# print(plus, num, imaginary)
	#
	# else:
	# 	minus = param.rfind("-")
	# 	num = int(param[:minus])
	# 	imaginary = int(param[minus:-1])
	#
	# 	# print(minus, num, imaginary)
	#
	# return (num, imaginary)




	# param = param.split()
	# temp = []
	# minus = False
	#
	# # v1
	# for i in enumerate(param):
	# 	if i[1] == "+":
	# 		continue
	# 	elif i[1] == "-":
	# 		minus = True
	# 		continue
	# 	temp.append(i[1])
	#
	# temp[-1] = temp[-1][:-1]
	#
	# if minus:
	# 	temp[-1] = int(temp[-1]) * -1
	# 	temp.append(temp[-1])
	# 	temp.pop()
	#
	# temp = tuple(list(map(int, temp)))
	# return temp

print(complex_to_tuple("1+2i"))
print(complex_to_tuple("6+9i"))
print(complex_to_tuple("-7-2i"))
print(complex_to_tuple("3-4i"))



# print(complex_to_tuple("1 + 2i"))
# print(complex_to_tuple("6 + 9i"))
# print(complex_to_tuple("-7 - 2i"))
# print(complex_to_tuple("3 - 4i"))




