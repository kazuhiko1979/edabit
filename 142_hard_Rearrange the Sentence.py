"""
Rearrange the Sentence
Given a sentence with numbers representing a word's location embedded within each word, return the sorted sentence.

Examples
rearrange("is2 Thi1s T4est 3a") ➞ "This is a Test"

rearrange("4of Fo1r pe6ople g3ood th5e the2") ➞ "For the good of the people"

rearrange(" ") ➞ " "
Notes
Only the integers 1-9 will be used.
"""
from string import digits

def rearrange(txt):

	# v3
	words = sorted(sorted(i, key=lambda x: x.isalpha()) for i in txt.split())
	print(words)
	return ' '.join(''.join(i[1:]) for i in words)


	# v2
	# txt = txt.split()
	# ret = [' ']*len(txt)
	# # print(ret)
	# for i in txt:
	# 	num = int([x for x in i if x.isdigit()][0])
	# 	# print(num)
	# 	ret[num-1] = ''.join([x for x in i if x.isalpha()])
	# 	# print(ret)
	#
	# return ' '.join(ret)


	# v1
	# result = []
	# count = 1
	# list_txt = txt.split()
	#
	# while len(list_txt) > 0:
	# 	for i in txt.split():
	# 		if str(count) in i:
	# 			remove_digits = str.maketrans('','',digits)
	# 			res = i.translate(remove_digits)
	# 			result.append(res)
	# 			list_txt.remove(i)
	# 			count += 1
	#
	# return ' '.join(result)

print(rearrange("is2 Thi1s T4est 3a"))
print(rearrange("4of Fo1r pe6ople g3ood th5e the2"))
print(rearrange(" "))