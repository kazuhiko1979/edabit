"""
Find All Digits
Taking each four digit number of a list in turn, return the number that you are on when all of the digits 0-9 have been discovered. If not all of the digits can be found, return "Missing digits!".

Examples
find_all_digits([5175, 4538, 2926, 5057, 6401, 4376, 2280, 6137, 8798, 9083]) ➞ 5057
# digits found:  517-  4-38  29-6  -0

find_all_digits([5719, 7218, 3989, 8161, 2676, 3847, 6896, 3370, 2363, 1381]) ➞ 3370
# digits found:  5719  -2-8  3---  --6-  ----  --4-  ----  ---0

find_all_digits([4883, 3876, 7769, 9846, 9546, 9634, 9696, 2832, 6822, 6868]) ➞ "Missing digits!"
# digits found:  48-3  --76  ---9  ----  -5--  ----  ----  2---
# 0 and 1 are missing
Notes
The digits can be discovered in any order.
"""
# v3
def find_all_digits(nums):

	digits = list('0123456789')
	for n in nums:
		for d in str(n):
			if d in digits:
				digits.remove(d)
				if not digits:
					return n
	return "Missing digits!"



# v2
# def find_all_digits(nums):
#
# 	s = set()
# 	for n in nums:
# 		for d in str(n):
# 			s.add(d)
# 		if len(s) == 10:
# 			return n
# 	return "Missing digits!"
#

# v1
# def find_all_digits(nums):
#
# 	digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 	result = []
#
# 	for num in nums:
# 		for i in str(num):
# 			if int(i) is not result:
# 				if int(i) in digits:
# 					result.append(int(i))
# 					digits.remove(int(i))
# 		if len(result) == 10:
# 			return num
# 	return "Missing digits!"


print(find_all_digits([5175, 4538, 2926, 5057, 6401, 4376, 2280, 6137, 8798, 9083]))
print(find_all_digits([5719, 7218, 3989, 8161, 2676, 3847, 6896, 3370, 2363, 1381]))
print(find_all_digits([4883, 3876, 7769, 9846, 9546, 9634, 9696, 2832, 6822, 6868]))