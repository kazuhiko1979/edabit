"""
Get Free Wi-Fi Anywhere You Go
A new 'hacky' phone is launched, which has the feature of connecting to any Wi-Fi network from any distance away, as long as there aren't any obstructions between the hotspot and the phone. Given a string, return how many Wi-Fi hotspots I'm able to connect to.

The phone is represented as a P.
A hotspot is represented as an *.
An obstruction is represented as a #. You cannot access a hotspot if they are behind one of these obstructions.
Examples
nonstop_hotspot("*   P  *   *") ➞ 3

nonstop_hotspot("*  * #  * P # * #") ➞ 1

nonstop_hotspot("***#P#***") ➞ 0
Notes
There will be only one phone.
No other characters, other than spaces, will appear in the tests.
"""
import re

def nonstop_hotspot(area):


	# v4
	ans = re.search(r'[* ]*P[* ]*', area)
	return ans.group().count('*')


	# v3
	# return [x.count("*") for x in area.split("#") if "P" in x][0]

	# v2
	# j, n = area.index('P'), 0
	# # print(j)
	# for i in range(j, -1, -1):
	# 	if area[i] == "#":
	# 		break
	# 	if area[i] == "*":
	# 		n += 1
	# for i in range(j, len(area)):
	# 	if area[i] == "#":
	# 		break
	# 	if area[i] == "*":
	# 		n += 1
	# return n


	# v1
	# top_count = 0
	# bottom_count = 0
	# top_index = 0
	# bottom_index = 0
	# top_P_index = area.rfind("P")
	# bottom_P_index = area[::-1].rfind("P")
	#
	# while top_index < top_P_index:
	# 	if area[top_index] == '*':
	# 		top_count += 1
	# 		top_index += 1
	# 	elif area[top_index] == '#':
	# 		top_count = 0
	# 		top_index += 1
	# 	else:
	# 		top_index += 1
	#
	# while bottom_index < bottom_P_index:
	# 	if area[::-1][bottom_index] == '*':
	# 		bottom_count += 1
	# 		bottom_index += 1
	# 	elif area[::-1][bottom_index] == '#':
	# 		bottom_count = 0
	# 		bottom_index += 1
	# 	else:
	# 		bottom_index += 1
	#
	# return top_count + bottom_count

print(nonstop_hotspot("*   P  *   *"))
print(nonstop_hotspot("*  * #  * P # * #"))
print(nonstop_hotspot('***#P#***'))
print(nonstop_hotspot('#P#'))
print(nonstop_hotspot('# *****  **  P     ** #    '))
