"""
Super-d Numbers
A number n becomes a super-d number when, for any digit d from 2 up to 9, the result of d * nᵈ contains d consecutive digits equal to d.

Given a positive integer n, implement a function that returns:

"Super-d Number" if n is a super-d number, replacing the letter d with the digit (any from 2 up to 9) that makes it super;
"Normal Number" if n is not a super-d number.
Examples
is_super_d(19) ➞ "Super-2 Number"
# when d = 2
# 2 * 19² = 722
# There are two (d) consecutives digits equal to 2 (d)

is_super_d(753) ➞ "Super-3 Number"
# when d = 3
# 3 * 753³ = 1280873331
# There are three (d) consecutives digits equal to 3 (d)

is_super_d(1168) ➞ "Super-4 Number"
# when d = 4
# 4 * 1168⁴ = 7444428488704
# There are four (d) consecutives digits equal to 4 (d)

is_super_d(24) ➞ "Normal Number"
# No cases where d * 24ᵈ (with d being any digit from 2 up to 9)...
# ...leads to a result containing d consecutive digits equal to d
Notes
Any given n will be a positive integer greater or equal to 0.
"""

def is_super_d(n):

	for i in range(2, 10):
		if str(i) * i in str(i * (n ** i)):
			return 'Super-{} Number'.format(i)
	return 'Normal Number'


	# top_super_d = []
	# super_d = []
	#
	# for i in range(2, 9):
	# 	result = str(num ** i * i)
	# 	temp = ''.join(sorted(result))
	# 	print(result)
	#
	# 	print(result[int(result.find(str(i)))])
	# 	# index
	# 	print(result[result.find(str(i)):])


# start_index = result.find(str(i))
		# print(start_index)



		# # print(temp.count(str(i)))
		# # print(i, temp.count(str(i)))
		#
		# if i <= temp.count(str(i)):
		# 	start_index = result.find(str(i))
		# 	print(start_index)
		# 	if len(set(result[start_index:start_index+i])) == 1:
		# 		print(True)
		# 		return i
		# 	else:
		# 		pass
		# else:
		# 	pass
			# 	for x in range(0, len(result)):
		# 		try:
		# 			# 先頭判断
		# 			if str(i) == result[x] and result[x] != result[x-1]:
		# 				if result[x] == result[x + 1]:
		# 					top_super_d.append(result[x])
		# 					pass
		# 			# 先頭以外判断
		# 			if str(i) == result[x] and result[x] == result[x+1]:
		# 				super_d.append(result[x])
		# 		except IndexError:
		# 			pass
		# else:
		# 	pass
		# # super_d Noneの場合
		# if super_d:
		# 	if i == (len(top_super_d) + len(super_d)) and i == int(set(top_super_d+super_d).pop()) :
		# 		return i
		# 	else:
		# 		pass
		# 	if x == len(result) - 1:
		# 		if i == len(top_super_d + super_d) and i == int(set(top_super_d+super_d).pop()):
		# 			return i
		# 		else:
		# 			top_super_d, super_d = [], []





# print(is_super_d(19))
# print(is_super_d(753))
# print(is_super_d(1168))
print(is_super_d(20379))
# print(is_super_d(1045361))