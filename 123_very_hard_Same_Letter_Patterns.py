"""
Same Letter Patterns
Create a function that returns True if two strings share the same letter pattern, and False otherwise.

Examples
same_letter_pattern("ABAB", "CDCD") ➞ True

same_letter_pattern("ABCBA", "BCDCB") ➞ True

same_letter_pattern("FFGG", "CDCD") ➞ False

same_letter_pattern("FFFF", "ABCD") ➞ False
"""




# def same_letter_pattern(txt1, txt2):
#
# 	lst_txt1_2 = []
# 	lst_txt1_2.append(txt1)
# 	lst_txt1_2.append(txt2)
# 	return help_same_letter_pattern(lst_txt1_2)
#
# def help_same_letter_pattern(lst):
#
# 	temp = {}
# 	patterns = 0
# 	result = ""
# 	total = []
# 	for txt in lst:
# 		for i in txt:
# 			if i not in temp:
# 				patterns += 1
# 				temp[i] = patterns
# 				result += str(temp[i])
# 			else:
# 				result += str(temp[i])
# 		total.append(result)
# 		temp = {}
# 		patterns = 0
# 		result = ""
# 	return len(set(total)) == 1

def same_letter_pattern(txt1, txt2):

	def generate_pattern(txt):
		temp = {}
		pattern = ""
		current_pattern = 1

		for char in txt:
			if char not in temp:
				temp[char] = current_pattern
				current_pattern += 1
			pattern += str(temp[char])

		return pattern

	return generate_pattern(txt1) == generate_pattern(txt2)


print(same_letter_pattern('ABAB', 'CDCD'))
print(same_letter_pattern('AAABBB', 'CCCDDD'))
print(same_letter_pattern('ABCBA', 'BCDCB'))

print(same_letter_pattern('FFGG', 'FFG'))
print(same_letter_pattern('FFGG', 'CDCD'))