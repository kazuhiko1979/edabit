"""
A block sequence in three dimensions. We can write a formula for this one:

Sequence Step 1 - 5

Create a function that takes a number (step) as an argument and returns the amount of blocks in that step.

Examples
blocks(1) ➞ 5

blocks(5) ➞ 39

blocks(2) ➞ 12
Notes
Step 0 obviously has to return 0.
The input is always a positive integer.
"""

def blocks(step):

    if step == 0:
        return 0

    num, blocks = 5, []
    lst = [i for i in range(step)]
    for i in lst:
        if i == 0:
            blocks.append(num)
        else:
            if i > 0:
                blocks.append(((num + blocks[i - 1]) + i) + 1)
    return blocks[-1]


# print(blocks(0))
# print(blocks(1))
# print(blocks(2))
# print(blocks(3))
# print(blocks(4))
print(blocks(5))
print(blocks(33))


