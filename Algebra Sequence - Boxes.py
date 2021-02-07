"""
Create a function that takes a number (step) as an argument and returns the amount of boxes in that step of the sequence.

Box Sequence Image

Step 0: Start with 0
Step 1: Add 3
Step 2: Subtract 1
Repeat Step 1 & 2 ...

Examples
box_seq(0) ➞ 0
box_seq(1) ➞ 3
box_seq(2) ➞ 2
"""
def box_seq(step):

    target = 0

    if step == 0:
        return 0

    elif step % 2:
        target += 3
        return box_seq(step-1) + 3
    else:
        target -= 1
        return box_seq(step-1) - 1

    return target

print(box_seq(0))
print(box_seq(1))
print(box_seq(2))