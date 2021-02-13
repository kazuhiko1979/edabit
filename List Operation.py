"""
Create a function that takes three parameters where:

x is the start of the range (inclusive).
y is the end of the range (inclusive).
n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n. Return an empty list if there are no numbers that are divisible by n.

Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []
"""
def list_operation(x, y, n):

    # lst = []
    #
    # for i in range(x, y+1):
    #     if not i % n:
    #         lst.append(i)
    # return lst

    return [i for i in range(x, y+1) if not i % n]

print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(15, 20, 7))