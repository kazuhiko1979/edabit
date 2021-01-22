"""
Create a function that takes two arguments.
Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.
makes10(9, 10) ➞ True
makes10(9, 9) ➞ False
makes10(1, 9) ➞ True
"""
def makes10(a, b):

    return 10 in (a, b) or a + b == 10


if __name__ == '__main__':
    print(makes10(9, 10))
    print(makes10(9, 9))




