"""
Modify Words
Create a function that takes a list of any length. Modify each element (capitalize, reverse, hyphenate).

Examples
edit_words(["new york city"]) ➞ ["YTIC KR-OY WEN"]

edit_words(["null", "undefined"]) ➞ ["LL-UN", "DENIF-EDNU"]

edit_words(["hello", "", "world"]) ➞ ["OLL-EH", "-", "DLR-OW"]

edit_words([""]) ➞ ["-"]
Notes
Input list values can be any type.
"""

def edit_words(lst):

	return [f(w) for w in lst]


def f(x):
	x = x[::-1].upper()
	ln = len(x) // 2
	if len(x) % 2 == 0:
		x = x[:ln] + '-' + x[ln:]
	else:
		x = x[:ln+1] + '-' + x[ln+1:]
	return x



	# lst = lst[0].split(' ')
	# lst = ' '.join(reversed(lst))
	# lst = lst.split(' ')
	# print(lst)
	# print(len(lst))
	# # reverse_sentence = ' '.join(reversed(words))
	# # print(reverse_sentence)
	#
	# # lst = [cha for cha in lst[0].split()[::-1]]
	# # print(lst)
	# temp = []
	# index_lst = 0
	# while index_lst < len(lst):
	# 	word = lst[index_lst][::-1].upper()
	# 	temp.append(word)
	# 	index_lst += 1
	# return ' '.join(temp)
	#
	# # for ch in range(0, len(lst):
	# # 	# ch = reversed(ch)
	# 	# print(ch)
	# 	# ch = ch.capitalize()
	# 	# result.append(ch)
	# # return ''.join(result)

print(edit_words(["new york city"]))
print(edit_words(["null", "undefined"]))
print(edit_words(["hello", "", "world"]))