"""
Simple Numbers
Mubashir needs your help to find the Simple Numbers in a given range.

A number X, that has an N amount of digits (which we'll enumerate as d1, d2, ..., dN), is Simple if the following equation holds true:

X = d1^1 + d2^2 + ... + dN^N
Examples of Simple Numbers:
89 = 8^1 + 9^2

135 = 1^1 + 3^2 + 5^3
Create a function which returns a list of all the Simple Numbers that exist within a given range between a and b (both numbers are inclusive).

Generate a list of the individual digits of the number.
Filter the list so that only "simple numbers" are kept.
To find out if a number is "simple":
Take the digits of the number.
For each digit, calculate digit ^ (index_of_the_digit + 1).
Sum the results of the calculations above and compare with the original number, if they're equal, the number is "simple".
Examples
simple_numbers(1, 10) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9]

simple_numbers(1, 100) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

simple_numbers(90, 100) ➞ []
"""

def simple_numbers(a, b):


    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]

    # simple = 0
    # result = []
    # for x in range(a, b+1):
    #     for i, d in enumerate(str(x), 1):
    #         simple += int(d)**i
    #     if x == simple:
    #         result.append(simple)
    #     simple = 0
    # return result




    # result = []
    # lst = [i for i in range(a, b+1)]
    # simple = 0
    #
    # for key, num in enumerate(lst, start=lst[0]):
    #     for x in range(0, len(str(num))):
    #         simple += int(str(num)[x]) ** (x+1)
    #     if key == simple:
    #         result.append(simple)
    #     simple = 0
    # return result

# print(simple_numbers(50, 150))
print(simple_numbers(88, 100))
# print(simple_numbers(100, 32253))
