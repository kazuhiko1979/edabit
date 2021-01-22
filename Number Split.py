"""
Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.
Examples
number_split(4) ➞ [2, 2]
number_split(10) ➞ [5, 5]
number_split(11) ➞ [5, 6]
number_split(-9) ➞ [-5, -4]
"""


def number_split(n):
    return [n // 2, n - n // 2]


if __name__ == '__main__':
    print(number_split(4))
    print(number_split(10))
    print(number_split(11))
    print(number_split(-9))

