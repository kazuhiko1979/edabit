"""
Are Pairs Sufficient for a Clear Ordering?
Create a function that returns True if an array of pairs are sufficient for a clear ordering of all items.

To illustrate:

clear_ordering([["D", "A"], ["C", "B"], ["A", "C"]]) ➞ True
# Since unequivocally: "D" < "A" < "C" < "B"
On the other hand:

clear_ordering([["D", "A"], ["B", "A"], ["C", "D"]]) ➞ False
# Since we know that "C" < "D" < "A", and we know "B" < "A"
# but we don't know anything about "B"s relationship with "C" or "D".
Examples
clear_ordering([["S", "T"], ["T", "U"], ["U", "V"]]) ➞ True

clear_ordering([["T", "S"], ["T", "U"], ["U", "V"], ["V", "W"]]) ➞ False
Notes
See Comments for a good visualization of the question.
"""

# v3
# import numpy as np
#
# def clear_ordering(lst):
#
# 	lst = np.array(lst).T.tolist()
# 	return len(set(lst[0])) == len(set(lst[1]))

# v2
def clear_ordering(lst):

	return len(set([x[0] for x in lst])) == len(set([y[1] for y in lst]))

# v1
	# lead_list = []
	# end_list = []
	#
	# for i in lst:
	# 	lead_list.append(i[0])
	# 	end_list.append(i[1])
	#
	# return len(set(lead_list)) == len(set(end_list))


print(clear_ordering([["D", "A"], ["C", "B"], ["A", "C"]]))
print(clear_ordering([["D", "A"], ["B", "A"], ["C", "D"]]))
print(clear_ordering([["S", "T"], ["T", "U"], ["U", "V"]]))
print(clear_ordering([["T", "S"], ["T", "U"], ["U", "V"], ["V", "W"]]))