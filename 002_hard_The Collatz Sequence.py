"""
The Collatz sequence is as follows:

Start with some given integer n.
If it is even, the next number will be n divided by 2.
If it is odd, multiply it by 3 and add 1 to make the next number.
The sequence stops when it reaches 1.
According to the Collatz conjecture, it will always reach 1. If that's true, you can construct a finite sequence following the aforementioned method for any given integer.

Write a function that takes in an integer n and returns the highest integer in the corresponding Collatz sequence.

Examples
max_collatz(10) ➞ 16
# Collatz sequence: 10, 5, 16, 8, 4, 2, 1

max_collatz(32) ➞ 32
# Collatz sequence: 32, 16, 8, 4, 2, 1

max_collatz(85) ➞ 256
# Collatz sequence: 85, 256, 128, 64, 32, 16, 8, 4, 2, 1
"""

def max_collatz(num):

    # no use max
    # res = num
    # while num > 1:
    #     num = num * 3 + 1 if num % 2 else num // 2
    #     if num > res:
    #         res = num
    # return res


    # seq = []
    # while num != 1:
    #     seq.append(num)
    #     num = num // 2 if num % 2 == 0 else num * 3 + 1
    # return max(seq) if seq else 1

def max_collatz_v1(num):

    res = []
    res.append(num)

    while num > 1:
        if num % 2 == 0:
            num = num / 2
            res.append(num)
        else:
            num = num * 3 + 1
            res.append(num)

    return max(res)


if __name__ == '__main__':

    print(max_collatz_v1(10))

# print(max_collatz(10))
# print(max_collatz(32))
# print(max_collatz(85))
# print(max_collatz(161))




