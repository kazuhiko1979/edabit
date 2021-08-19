"""
Mubashir was trying to understand Divisibility Rule on Wikipedia which states :

"A divisibility rule is a shorthand way of determining whether a given integer is divisible by a fixed divisor without performing the division, usually by examining its digits."

He came up with an important fact for Divisibility by 13 rule on Wikipedia, which states that if you divide the successive powers of 10 by 13 you get the following remainders :

10^0 % 13 = 1
10^1 % 13 = 10
10^2 % 13 = 9
10^3 % 13 = 12
10^4 % 13 = 3
10^5 % 13 = 4
10^6 % 13 = 1 (repetition starts from here)
They concluded the following method:

Multiply the right-most digit of the number with the left-most number in the sequence shown above and the second right-most digit to the second left-most digit of the number in the sequence and so on.
Sum up all these products.
Repeat this process until the sum remains constant.
What is the remainder when 1234567 is divided by 13?

7      6     5      4     3     2     1  (digits of 1234567 from the right)
×      ×     ×      ×     ×     ×     ×  (multiplication)
1     10     9     12     3     4     1  (repeating sequence)
We get:

7×1 + 6×10 + 5×9 + 4×12 + 3×3 + 2×4 + 1×1 = 178
Repeat same process with 178:

8x1 + 7x10 + 1x9 = 87
Repeat same process with 87:

7x1 + 8x10 = 87 (repetition starts from here)
Create a function that processes this sequence of operations on the given integer n and returns the final constant value.

Examples
divisibility_rule(1234567) ➞ 87

divisibility_rule(8529) ➞ 79

divisibility_rule(85299258) ➞ 31
"""

def divisibility_rule(n):

    n = str(n)[::-1]

    while len(str(n)) > 2:

        n_list = ([str(int(x)) for x in str(n)])
        seq_list = ([str(10 ** i % 13) for i in range(0, len(str(n)))])

        n = (sum([int(n) * int(s) for n, s in zip(n_list, seq_list)]))
        n = str(n)[::-1]

    n = str(n)[::-1]

    return int(n)

print(divisibility_rule(1234567))
print(divisibility_rule(8529))
print(divisibility_rule(85299258))














