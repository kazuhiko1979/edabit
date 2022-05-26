"""
Sorting Band Names without Articles
Create a function that sorts the given array of band names discounting the articles "The", "A", "An" if the first word of the name categorically belongs to.

Examples
band_names_sort(["The New Yardbirds", "The Beatles", "The Square Roots", "On A Friday", "An Irony"])
➞ ["The Beatles", "An Irony", "The New Yardbirds", "On A Friday", "The Square Roots"]

band_names_sort(["The Platters", "A Yard of Yarn", "The Everly Brothers", "A Monster Effect", "The Sex Maggots"])
➞ ["The Everly Brothers", "A Monster Effect", "The Platters", "The Sex Maggots", "A Yard of Yarn"]

band_names_sort(["But Myth", "An Old Dog", "Def Leppard", "The Any Glitters", "The Dawn"])
➞ ["The Any Glitters", "But Myth", "The Dawn", "Def Leppard", "An Old Dog"]
Notes
You have to return the sorted full band names.
"""
import re

def band_names_sort(lst):

	# v4
	return sorted(lst, key=lambda w: re.sub('^(A |An |The )', '', w))


	# v3
	# Recursion
	# def remove(n):
	# 	for i in ["The", "A", "An"]:
	# 		n = n.replace(i+" ", "")
	# 	return n
	# return sorted(lst, key=remove)



	# v2
	# articles = ["The", "A", "An"]
	# temp = []
	#
	# for txt in lst:
	# 	for i in txt.split():
	# 		if i in articles:
	# 			temp.append(re.sub(i, "", txt).lstrip())
	# 			break
	# 		else:
	# 			temp.append(txt.lstrip())
	# 			break
	#
	# return [i for x in sorted(temp) for i in lst if re.search(x, i)]



	# v1
	# articles = ["The", "A", "An"]
	# temp = []
	# for txt in lst:
	# 	for i in txt.split():
	# 		if i in articles:
	# 			txt = re.sub(i, "", txt)
	# 			txt = txt.lstrip()
	# 			temp.append(txt)
	# 			break
	# 		else:
	# 			txt = txt.lstrip()
	# 			temp.append(txt)
	# 			break
	# temp = sorted(temp)
	#
	# result = []
	#
	# for x in temp:
	# 	for i in lst:
	# 		if re.search(x, i):
	# 			result.append(i)
	# return result




print(band_names_sort(["The New Yardbirds", "The Beatles", "The Square Roots", "On A Friday", "An Irony"]))
print(band_names_sort(["The Platters", "A Yard of Yarn", "The Everly Brothers", "A Monster Effect", "The Sex Maggots"]))

print(band_names_sort(["But Myth", "An Old Dog", "Def Leppard", "The Any Glitters", "The Dawn"]))



# print(band_names_sort(["Platters", "Yard of Yarn", "Everly Brothers", "Monster Effect", "Sex Maggots"]))
# print(band_names_sort(["But Myth", "Old Dog", "Def Leppard", "Any Glitters", "Dawn"]))
