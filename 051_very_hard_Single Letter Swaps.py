"""
Single Letter Swaps
Given an array of strings and an original string, write a function to output an array of boolean values - True if the word can be formed from the original word by swapping two letters only once and False otherwise.

Examples
validate_swaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE")
➞ [True, True, False, False]

# Swap "A" and "B" from "ABCDE" to get "BACDE".
# Swap "A" and "E" from "ABCDE" to get "EBCDA".
# Both "BCDEA" and "ACBED" cannot be formed from "ABCDE" using only a single swap.

validate_swaps(["32145", "12354", "15342", "12543"], "12345")
➞ [True, True, True, True]

validate_swaps(["9786", "9788", "97865", "7689"], "9768")
➞ [True, False, False, False]
Notes
Original string will consist of unique characters.
"""
# v2
def validate_swaps(lst, txt):

	count = 0
	temp = []

	for j in lst:
		try:
			for i in range(len(j)):
				if j[i] == txt[i]:
					count += 1
			if count == len(txt)-2 and len(txt) == len(j):
				temp.append(True)
				count = 0
			else:
				temp.append(False)
				count = 0
		except:
			IndexError

	return temp






# v1
# def validate_swaps(lst, txt):
#
# 	result = []
# 	pivot = 0
# 	index = 0
#
# 	while index < len(lst):
# 		word = list(lst[index])
# 		try:
# 			for k in range(0, len(word)):
# 				word[pivot], word[k] = word[k], word[pivot]
# 				if ''.join(word) == txt:
# 					result.append(True)
# 					index += 1
# 					pivot = 0
# 					break
# 				else:
# 					word[k], word[pivot] = word[pivot], word[k]
# 				if k == len(word) - 1:
# 					pivot += 1
# 		except:
# 			result.append(False)
# 			index += 1
#
# 	return result


print(validate_swaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE"))
print(validate_swaps(["34145", "12354", "15342", "12543"], "12345"))
print(validate_swaps(["9786", "9788", "97865", "7689"], "9768"))
print(validate_swaps(['132', '321', '213'], '123'))