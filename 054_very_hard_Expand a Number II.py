"""
Expand a Number II
Create a function that expands a decimal number into a string as shown below:

25.24 ➞ "20 + 5 + 2/10 + 4/100"
70701.05 ➞ "70000 + 700 + 1 + 5/100"
685.27 ➞ "600 + 80 + 5 + 2/10 + 7/100"
Examples
expanded_form(87.04) ➞ "80 + 7 + 4/100"

expanded_form(123.025) ➞ "100 + 20 + 3 + 2/100 + 5/1000"

expanded_form(50.270) ➞ "50 + 2/10 + 7/100"
"""
# v4
def expanded_form(num):

	a, b = str(num).split('.')
	r = [k + '0' * (len(a) - 1 - i) for i, k in enumerate(a) if k != '0'] + \
		[k + '/1' + '0'*(i+1) for i, k in enumerate(b) if k != '0']

	return ' + '.join(r)


# v3
# def expanded_form(num):
#
# 	num = str(num)
# 	point = num.index(".")
#
# 	result = []
# 	for i, x in enumerate(num):
# 		if x not in "0.":
# 			if i < point:
# 				result.append(str(int(x) * 10 ** (point - i - 1)))
# 			else:
# 				result.append(x + "/" + str(10 ** (i - point)))
# 	return ' + '.join(result)

# v2
# def expanded_form(num):
#
# 	sep_num = str(num).split('.')
# 	num_int = [n + '0' * k for k, n in enumerate(reversed(sep_num[0])) if (n + '0' * k)[0] != '0'][::-1]
# 	num_float = [(n + '/' + '1' + '0' * k) for k, n in enumerate(sep_num[1], start=1) if (n + '/' + '1' + '0' * k)[0] != '0']
#
# 	return ' + '.join(num_int + num_float)

	# v1
	# for k, n in enumerate(reversed(sep_num[0])):
	# 	i = n + '0' * k
	# 	if i != '0':
	# 		temp.append(i)
	# temp = temp[::-1]
	#
	# for k, n in enumerate(sep_num[1], start=1):
	# 	i = n + '/' + '1' + '0' * k
	# 	if i[0] != '0':
	# 		temp.append(i)
	#
	# print(temp)

print(expanded_form(87.04))
print(expanded_form(123.025))
print(expanded_form(50.270))

print(expanded_form(207.333))
