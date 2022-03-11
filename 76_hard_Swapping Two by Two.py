"""
Swapping Two by Two
Write a function that swaps the first pair (1st and 2nd characters) with the second pair (3rd and 4th characters) for every quadruplet substring.

Examples
swap_two("ABCDEFGH") ➞ "CDABGHEF"

swap_two("AABBCCDDEEFF") ➞ "BBAADDCCFFEE"

swap_two("munchkins") ➞ "ncmuinhks"

swap_two("FFGGHHI") ➞ "GGFFHHI"
Notes
Keep leftover strings in the same order.
"""

def swap_two(txt):

	# swapped = ""
	# for i in range(0, len(txt), 4):
	# 	a, b = txt[i+2:i+4], txt[i:i+2]
	# 	swapped += (b + a) if len(a + b) < 4 else (a + b)
	# return swapped


	ans = []
	while len(txt) >= 4:
		ans.append(txt[2:4])
		ans.append(txt[0:2])
		txt = txt[4:]
	if txt:
		ans.append(txt)
	return ''.join(ans)





print(swap_two("ABCDEFGH"))
print(swap_two("AABBCCDDEEFF"))