"""
Decompose Address
Create a function that decomposes an address string into a list of five substrings:

Street Number
Street Name
City Name
State
Zip Code
Examples
decompose_address("557 Farmer Rd Corner, MT 59105")
➞ ["557", "Farmer Rd", "Corner", "MT", "59105"]

decompose_address("3315 Vanity St Beverly Hills, CA 90210")
➞ ["3315", "Vanity St", "Beverly Hills", "CA", "90210"]

decompose_address("8919 Scarecrow Ct Idaho Falls, ID 80193")
➞ ["8919", "Scarecrow Ct", "Idaho Falls", "ID", "80193"]
Notes
All street extensions will be shortened to two-letter formats.
"""

import re

def decompose_address(txt):

	pattern = r'\d+|\b[A-Z][a-z]\w+\s*\w+|[A-Z]+'
	return re.findall(pattern, txt)

	# pattern = "[A-Z]{1}[a-z]{1}"
	#
	# res = re.findall(pattern, txt)
	# print(res)
	#
	# result = []
	# temp = txt.split()
	# result.append(temp[0])
	# print(result)
	#
	# Street_Name = ""
	# print(temp[1:])
	# for i, y in zip(res, temp[1:-2]):
	# 	Street_Name += y + " "
	# 	if i == y:
	# 		break
	# Street_Name = Street_Name[:-1]
	# result.append(Street_Name)
	# print(result)



	# return txt.extract('(\D+)\s+(\d+)\s?(.*)')


	# Street_Number = []
	# Street_Name = []
	# City_Name = []
	# State = []
	# Zip_Code =[]
	# # print(txt.split())
	#
	# result = []
	#
	# for k, v in enumerate(txt.split()):
	# 	if k == 0:
	# 		Street_Number.append(v)
	# 	if k == 1:
	# 		Street_Name.append(v)
	# 	if k == 2:
	# 		Street_Name.append(v)
	# 	if k == 3:
	# 		City_Name.append(v)
	# 	if k == 4:
	# 		State.append(v)
	# 	if k == 5:
	# 		Zip_Code.append(v)
	#
	# result.append(Street_Number)
	# result.append([' '.join(Street_Name)])
	# result.append(City_Name)
	# result.append(State)
	# result.append(Zip_Code)
	#
	# # print(result)
	#
	#
	# flatList = [item for elem in result for item in elem]
	# return flatList




print(decompose_address("3315 Vanity St Beverly Hills, CA 90210"))
print(decompose_address("557 Farmer Rd Corner, MT 59105"))
print(decompose_address("8919 Scarecrow Ct Idaho Falls, ID 80193"))