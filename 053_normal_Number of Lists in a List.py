"""
Return the total number of lists inside a given list.

Examples
num_of_sublists([[1, 2, 3]]) ➞ 1

num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 3

num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 4

num_of_sublists([1, 2, 3]) ➞ 0
"""

def num_of_sublists(lst):

    # return str(lst).count('[') - 1

    # count = 0
    # for i in lst:
    #     if isinstance(i, list):
    #         count += 1
    # return count


    # return sum(isinstance(i, list) for i in lst)


    # return sum(1 for i in lst if type(i) == list)


    # res = []
    #
    # for x in [i for i in lst]:
    #     if not str(x).isdecimal():
    #         res.append(x)
    #     else:
    #         return 0
    # return len(res)


print(num_of_sublists([[1, 2, 3]]))
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(num_of_sublists([1, 2, 3]))
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
