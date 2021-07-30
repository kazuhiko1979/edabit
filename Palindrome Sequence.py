"""
A palindrome is a number that is the same when reversed, 2770772 for example. A palindrome can often be formed by adding a number to it's reverse: 641 + 146 = 787 (a palindrome). Using 78 as the seed, it takes 4 steps to produce a palindrome:

78 + 87 = 165
165 + 561 = 726
726 + 627 = 1353
1353 + 3531 = 4884 (a palindrome)
About 97% of integers less than 10,000 produce palindromes in less than 25 steps. A few, like 196 and 879, may never form palindromes.

Make a function that takes a palindrome as it's an argument and returns the smallest seed integer that will produce that palindrome, along with the number of steps required:

pal_seq(palindrome) = (seed, steps)
pal_seq(4884) ➞ (69, 4)

pal_seq(1) ➞ (1, 0)

pal_seq(11) ➞ (10, 1)
# 10 + 01 = 11

pal_seq(3113) ➞ (199, 3)

pal_seq(8836886388) ➞ (177, 15)
Notes
The sequence always terminates when the first palindrome is produced. If the seed is a palindrome, the sequence has 0 steps.
"""


def pal_seq(n):


    for i in range(1, n + 1):
        p, count = i, 0
        while i < n and int(str(i)[::-1]) - i:
            i += int(str(i)[::-1])
            count += 1
        if i == n:
            break

    return p, count

print(pal_seq(4884))
print(pal_seq(3113))






