"""
Traveling through Europe one needs to pay attention to how the license plate in the given country is displayed. When crossing the border you need to park on the shoulder, unscrew the plate, re-group the characters according to the local regulations, attach it back and proceed with the journey.

Create a solution that can format the dmv number into a plate number with correct grouping. The function input consists of a string s and group length n. The output has to be upper case characters and digits. The new groups are made from right to left and connected by -. The original order of the dmv number is preserved.

Examples
license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"

license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"

license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"

license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"
"""
import re

def license_plate(s, n):

	# v3
	s = s.replace("-", "")[::-1].upper()
	return '-'.join([s[i:i+n] for i in range(0, len(s), n)][::-1])

	# v2
	# s = s.upper().replace("-", "")
	# res = []
	# while len(s) > n:
	# 	res.append(s[-n:])
	# 	s = s[:-n]
	# if len(s) > 0:
	# 	res.append(s)
	# return "-".join(res[::-1])


	# v1
	# s = re.split('(' + '.' * n + ')', ''.join(list(reversed(s))).replace('-', ''))
	# return ('-'.join([j.upper() for j in [x for x in [i[::-1] for i in s][::-1]] if j != '']))


print(license_plate("5F3Z-2e-9-w", 4))
print(license_plate("2-5g-3-J", 2))
print(license_plate("2-4A0r7-4k", 3))
print(license_plate("nlj-206-fv", 3))
print(license_plate("GB-bd519-KFC", 2))
print(license_plate("d-kapa-7778", 4))