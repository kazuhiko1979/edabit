"""
A Collatz sequence is generated by repeatedly applying the following rules to an integer and then to each resulting integer in turn:

If even: divide by 2.
If odd: multiply by 3, then add 1.
The Collatz conjecture states that, for any initial positive integer, you will eventually reach the number 1.

Write a function that, for an initial positive integer n, returns a list containing 2 values:

The number of times the Collatz rule has to be applied until you reach 1.
The maximum number reached in the process.
Examples
collatz(17) ➞ [12, 52]
# Because 17 – 52 – 26 – 13 – 40 – 20 – 10 – 5 – 16 – 8 – 4 – 2 – 1
# takes 12 steps and 52 is the highest number reached.

collatz(6) ➞ [8, 16]

collatz(21) ➞ [7, 64]
"""
# import copy
# res = []

def collatz(n):

    l = [n]
    while n > 1:
        n = 3 * n + 1 if n % 2 else n / 2
        l.append(n)
    return [len(l)-1, max(l)]

    # count = 0
    # max = n
    # while n!= 1:
    #     if n % 2 == 0:
    #         n /= 2
    #     else:
    #         n = n * 3 + 1
    #
    #     if max < n:
    #         max = n
    #
    #     count += 1
    #
    # return [count, max]


    # M = n
    # it = 0
    # while n != 1:
    #     if n % 2:
    #         n = 3 * n + 1
    #     else:
    #         n //= 2
    #     it += 1
    #     M = max(n, M)
    # return [it, M]


#     while n > 1:
#         if n % 2 == 0:
#             return divide(n)
#         elif n % 2 == 1:
#             return multiply(n)
#
#     if res == []:
#         return [0, int(n)]
#     else:
#         result = copy.deepcopy(res)
#         res.clear()
#     return [len(result), max(result)]
#
#
# def divide(n):
#     n = n / 2
#     res.append(int(n))
#     return collatz(n)
#
# def multiply(n):
#     n = n * 3 + 1
#     res.append(int(n))
#     return collatz(n)

print(collatz(1))
print(collatz(3))
print(collatz(9))
print(collatz(27))
print(collatz(81))

