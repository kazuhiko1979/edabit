"""
Where Are My Glasses?
Oh no! I've lost my glasses, but paradoxically, I need glasses to find my glasses!

Please help me out by showing me the index in the list which contains my glasses. They look like two capital Os, with any number of dashes in between!

This means that both O--O and O------------O are valid glasses, but not O----#--O for example!
Search thoroughly, maybe you'll find my glasses in places such as 'dustO-Odust'
Examples
find_glasses(["phone", "O-O", "coins", "keys"]) ➞ 1

find_glasses(["OO", "wallet", "O##O", "O----O"]) ➞ 3

find_glasses(["O--#--O", "dustO---Odust", "more dust"]) ➞ 1
Notes
All lists will include one valid pair of glasses because I swear I dropped them around here somewhere ...
All elements in the list are strings.
"""
# v2
import re

def find_glasses(lst):

	for idx, i in enumerate(lst):
		if re.search('O-+O', i):
			return idx


# v1
# def find_glasses(lst):
#
# 	up_zero = []
# 	line = []
# 	bottom_zero = []
#
# 	for words in lst:
# 		if len(set(words)) == 1:
# 			up_zero = []
# 			line = []
# 			bottom_zero = []
# 			continue
# 		for word in words:
# 			if not up_zero:
# 				if word == 'O':
# 					up_zero.append(word)
# 			if up_zero:
# 				if word == '-':
# 					line.append(word)
# 			if up_zero:
# 				if line:
# 					if not bottom_zero:
# 						if word == 'O':
# 							bottom_zero.append(word)
# 							return lst.index(words)
# 			if word != 'O' and word != '-':
# 				if up_zero:
# 					line = []
# 					up_zero = []

print(find_glasses(['phone', 'O-O', 'coins', 'keys']))
print(find_glasses(['OO', 'wallet', 'O##O', 'O----O']))
print(find_glasses(['O_O', 'O-O', 'OwO']))
print(find_glasses(['O--#--O', 'dustO---Odust', 'more dust']))
print(find_glasses(['floor', 'the floor again', 'pockets', 'bed', 'cabinet', 'the top of my head O-O']))
print(find_glasses(['OOOO----~OOO', '-------', 'OOOOOOO', 'OO-OO-OO-O']))