"""
Party People Part I: Make it Recursive
Ava, Mark, Sheila, and Pete are at a party. However, Ava and Sheila are only staying if there are at least 4 people, Pete is only staying if there's 1 person, and Mark is only staying if there are at least 5 people. Therefore, Mark leaves, which makes Ava and Sheila leave, and Pete is left alone.

Given a list with the preferences of every person at a party for the minimum number of people present, determine how many people will stay.

It is required that you solve this challenge recursively.

Examples
party_people([4, 5, 4, 1]) ➞ 1
# Ava's minimum number is 4, Mark's is 5, Sheila's is 4, and Pete's is 1.
# Only 1 person (Pete) stays.

party_people([10, 12, 15, 15, 5]) ➞ 0

party_people([2, 1, 2, 0]) ➞ 4
Notes
All attendees are included in the list.
Any person's count includes themself.
Expect valid input only.
"""

def party_people(lst):

	# v2
	if lst and max(lst) > len(lst):
		lst.pop(lst.index(max(lst)))
		return party_people(lst)
	else:
		return len(lst)


	# v1
	# lst_after_leaves = [i for i in lst if i <= len(lst)]
	#
	# if lst == lst_after_leaves:
	# 	return len(lst)
	# else:
	# 	return party_people(lst_after_leaves)

print(party_people([4, 5, 4, 1]))
print(party_people([10, 12, 15, 15, 5]))
print(party_people([2, 1, 2, 0]))

