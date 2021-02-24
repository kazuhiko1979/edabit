"""
Create a function that squares every digit of a number.

Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer.
"""


def square_digits(n):

    result = [int(i)**2 for i in str(n)]
    result = int(''.join(map(str, result)))
    return result


print(square_digits(9119))
print(square_digits(2483))
print(square_digits(3212))

