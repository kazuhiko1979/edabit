"""
Bridge Shuffle
Create a function to bridge shuffle two lists. To bridge shuffle, you interleave the elements from both lists in an alternating fashion, like so:

List 1 = ["A", "A", "A"]
List 2 = ["B", "B", "B"]

Shuffled List = ["A", "B", "A", "B", "A", "B"]
This can still work with two lists of uneven length. We simply tack on the extra elements from the longer list, like so:

List 1 = ["C", "C", "C", "C"]
List 2 = ["D"]

Shuffled List = ["C", "D", "C", "C", "C"]
Create a function that takes in two lists and returns the bridge-shuffled list.

Examples
bridge_shuffle(["A", "A", "A"], ["B", "B", "B"]) ➞ ["A", "B", "A", "B", "A", "B"]

bridge_shuffle(["C", "C", "C", "C"], ["D"]) ➞ ["C", "D", "C", "C", "C"]

bridge_shuffle([1, 3, 5, 7], [2, 4, 6]) ➞ [1, 2, 3, 4, 5, 6, 7]
Notes
Elements in both lists can be strings or integers.
If two lists are of unequal length, add the additional elements of the longer list to the end of the shuffled list.
Always start your shuffle with the first element of List 1.
"""
from itertools import zip_longest


def bridge_shuffle(lst1, lst2):

    # step = 1
    # for x in lst2:
    #     lst1.insert(step, x)
    #     step += 2
    # return lst1


    # result = []
    # for item1, item2 in zip_longest(lst1, lst2):
    #     if item1:
    #         result.append(item1)
    #     if item2:
    #         result.append(item2)
    # return result


    for i, n in enumerate(lst2):
        lst1.insert(i+i+1, n)
    return lst1



    # res = itertools.zip_longest(lst1, lst2, fillvalue='')
    #
    # if str(lst1[0]).isdigit():
    #
    #     res = list(itertools.zip_longest(lst1, lst2))
    #     tmp = []
    #     for i in res:
    #         tmp.append(i[0])
    #         tmp.append(i[1])
    #     tmp.remove(None)
    #     return tmp
    #
    # else:
    #     res = list(map(str, list(''.join([''.join(i) for i in res]))))
    #
    # return res

print(bridge_shuffle(["A", "A", "A"], ["B", "B", "B"]))
print(bridge_shuffle(['C', 'C', 'C', 'C'], ['D']))
print(bridge_shuffle([1, 3, 5, 7], [2, 4, 6]))
print(bridge_shuffle([10, 9, 8], [1, 2, 3, 4]))
print(bridge_shuffle([1, 3, 5, 7], [2, 4, 6]))



