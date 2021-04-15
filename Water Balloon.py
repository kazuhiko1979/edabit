"""
Once a water balloon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.

The effect of a water balloon popping can be modeled using a list. Create a function that takes a list which takes the pre-pop state and returns the state after the balloon is popped. The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element.

Examples
pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]

pop([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]

pop([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]

pop([0]) ➞ [0]
Notes
Length of input list is always odd.
The input list will always be the exact length it takes for there to be exactly one border zero.
If the input list consists only of zeroes, return the same list.
"""
import numpy as np


def pop(state):

    res = []
    center = int((np.ceil(len(state) / 2)) - 1)
    inc_list = list([i for i in range(center)])
    reversed_list = list(reversed(inc_list))
    res.append(center)
    return inc_list + res + reversed_list


print(pop([0, 0, 0, 0, 4, 0, 0, 0, 0]))
print(pop([0, 0, 0, 3, 0, 0, 0]))
print(pop([0, 0, 2, 0, 0]))
print(pop([0]))


