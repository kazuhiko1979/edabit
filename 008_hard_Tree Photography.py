"""
Heading off to the Tree Arboretum of Various Heights, I bring along my camera to snap up a few photos. Ideally, I'd want to take a picture of as many trees as possible, but the taller trees may cover up the shorter trees behind it.

A tree is hidden if it is shorter or the same height as the tree in front.

Given a list of tree heights, create a function which returns "left" or "right", depending on which side allows me to see as many trees as possible.

Worked Example
tree_photography([1, 3, 1, 6, 5]) ➞ "left"

# If I stand on the left, I can see trees of heights 1, 3 and 6.
# If I stand on the right, I can see trees of heights 5 and 6.
# Return "left" because I would see more trees.
Examples
tree_photography([5, 6, 5, 4]) ➞ "right"

tree_photography([1, 2, 3, 3, 3, 3, 3]) ➞ "left"

tree_photography([3, 1, 4, 1, 5, 9, 2, 6]) ➞ "left"
Notes
There will always be a best side.
"""

def count_trees(lst):

    n_trees = 1
    max_height = lst[0]
    for t in lst[1:]:
        if t > max_height:
            n_trees += 1
            max_height = t
    return n_trees

def tree_photography(trees):

    return "left" if count_trees(trees) > count_trees(trees[::-1]) else "right"



#     unique_trees = sorted(set(trees), key=trees.index)
#
#     left_num = unique_trees.index(max(trees))
#     right_num = unique_trees[::-1].index(max(trees))
#
# # Python 3.7以前では、dictによるsortedの保証はない
# # left_num = list(dict.fromkeys(trees)).index(max(trees))
# # right_num = list(dict.fromkeys(trees[::-1])).index(max(trees))
# #
#     return "left" if left_num > right_num else "right"

print(tree_photography([1, 2, 3, 6, 5]))