"""
Recursion: License Plate
Traveling through Europe one needs to pay attention to how the license plate in the given country is displayed. When crossing the border you need to park on the shoulder, unscrew the plate, re-group the characters according to the local regulations, attach it back and proceed with the journey.

Create a solution that can format the dmv number into a plate number with correct grouping. The function input consists of string s and group length n. The output has to be upper case characters and digits. The new groups are made from right to left and connected by -. The original order of the dmv number is preserved.

Examples
license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"

license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"

license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"

license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"
"""
# v2
import re

def license_plate(code, n):

	code = code.upper()
	code = re.sub('-', '', code)

	if len(code) <= n:
		return code
	return license_plate(code[:-n], n) + '-' + code[-n:]






# v1
# import copy
#
# def license_plate(code, group):
#
# 	code = code.replace("-", "").upper()
# 	return license_plate_helper(code, group)
#
# def license_plate_helper(code, group, temp=[]):
#
# 	while len(code) > group:
# 		temp.append(code[-group:])
# 		code = list(code)[:-group]
# 		code = "".join(code)
# 		return license_plate_helper(code, group, temp)
# 	else:
# 		temp.append(code)
#
# 	result = copy.deepcopy(temp)
# 	temp.clear()
# 	result = "-".join(result[::-1])
# 	return result

print(license_plate("5F3Z-2e-9-w", 4))
print(license_plate("2-5g-3-J", 2))
print(license_plate("2-4A0r7-4k", 3))
print(license_plate("nlj-206-fv", 3))
print(license_plate("GB-bd519-KFC", 2))
