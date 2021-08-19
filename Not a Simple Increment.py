"""
Create a function that takes three integer parameters: a number n, number of iterations, and step. You have to implement an algorithm, which increases the given number as explained below:

n = 143726, iterations = 16, step = 3
simpleIncrement(n, iterations, step) ➞ 243826
Step 1: We start from the first digit and increment the 4th digit because the step is 3.

s - Starting Position
* - current increased position

Position: s - - - - - ➞ - - - * - -
Number:   1 4 3 7 2 6 ➞ 1 4 3 8 2 6
Step 2: Repeat step #1 with the updated starting position.

s - Starting Position
* - current increased position

Position: - - - s - - ➞ * - - - - -
Number:   1 4 3 8 2 6 ➞ 2 4 3 8 2 6
Remember, if the number overflows, the current position gets shifted to the right.
9 9 9 ➞ - - p   // before overflow position will be at 3rd digit
1 0 0 0 ➞ - - - p   // after overflow position will be at 4th digit
More examples on overflow:
9 ➞ 10
799 ➞ 800 (If you increased the second 9) or 809 (if you increased the first 9)
99000 ➞ 100000 (If you increased the second 9) or 109000 (if you increased the first 9)
Examples
simple_increment(1673, 2, 16) ➞ 3673

simple_increment(99, 99, 99) ➞ 198

simple_increment(99, 99, 98) ➞ 4734
"""

def simple_increment(n, iterations, step):

    i = 0

    while iterations > 0:

        n_length = len(str(n))
        i = (i + step) % n_length
        a = n_length - i - 1
        n += 10**a

        if n_length != len(str(n)):
            i += 1
        iterations -= 1
    return n


print(simple_increment(1673, 2 , 16))








