"""
Recursion: Case and Index Inverter
Write a recursive function that takes a string input and returns the string in a reversed case and order.

Examples
invert("dLROW YM sI HsEt") ➞ "TeSh iS my worlD"

invert("ytInIUgAsnOc") ➞ "CoNSaGuiNiTY"

invert("step on NO PETS") ➞ "step on NO PETS"

invert("XeLPMoC YTiReTXeD") ➞ "dExtErIty cOmplEx"
Notes
No empty strings and will neither contain special characters nor punctuation.
You are expected to solve this challenge using a recursive approach.
You can check on the Resources tab for more details about recursion.
"""
def invert(s):
	if not s:
		return s
	return invert(s[1:]) + s[0].swapcase()

# v2
# def opposite(s):
# 	return s.lower() if s.isupper() else s.upper()
#
# def invert(s):
# 	if not s:
# 		return ""
# 	else:
# 		return opposite(s[-1]) + invert(s[:-1])




# v1
# def invert(s, result=[]):
	# while s:
	# 	if s[::-1][0].isupper():
	# 		result.append(s[::-1][0].lower())
	# 		return invert(s[:-1], result)
	# 	if s[::-1][0].islower():
	# 		result.append(s[::-1][0].upper())
	# 		return invert(s[:-1], result)
	# 	if s[::-1][0] == " ":
	# 		result.append(" ")
	# 		return invert(s[:-1], result)
	# else:
	# 	original = ''.join(result)
	# 	result.clear()
	# 	return original

print(invert("dLROW YM sI HsEt"))
print(invert("ytInIUgAsnOc"))
print(invert("step on NO PETS"))
print(invert("XeLPMoC YTiReTXeD"))
