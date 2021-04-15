"""
Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).

Examples
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
Notes
The frequency of the majority element must be strictly greater than 1/2.
If there is no majority element, return None.
If the list is empty, return None.
"""
import collections


def majority_vote(lst):

    # print(len(list(set(lst)))) == 1

    count = collections.Counter(lst)
    original_dict = dict(count.most_common())


    # print(count.most_common())
    # print(sorted(sorted(original_dict.items(), key=lambda x:x[1])))
    if len(list(set(lst))) == 0:
        return None
    elif len(list(set(lst))) > 1 and count.most_common() == sorted(original_dict.items(), key=lambda x:x[1]):
        return None
    else:
        return count.most_common()[0][0]

print(majority_vote(["A", "B", "B", "B", "A", "A"]))
print(majority_vote(["B", "B", "B"]))
print(majority_vote(["B", "A", "B", "B", "C", "A", "B", "B"]))
print(majority_vote(["A", "B", "B"]))
print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "B"]))
print(majority_vote([]))

