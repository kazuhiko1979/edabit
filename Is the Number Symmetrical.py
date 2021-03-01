"""
Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.

Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
"""
def is_symmetrical(num):

    strNum = f'{num}'
    strNum = "{}".format(num)

    return strNum[::-1] == strNum


print(is_symmetrical(7227))
print(is_symmetrical(12567))
print(is_symmetrical(44444444))
print(is_symmetrical(9939))

