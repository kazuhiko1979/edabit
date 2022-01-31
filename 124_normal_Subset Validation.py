"""
Subset Validation
Write a function that returns True if all subsets in a list belong to a given set.

Examples
validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]) ➞ True

validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]) ➞ True

validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]) ➞ False

validate_subsets([[1, 2, 3, 4]], [1, 2, 3]) ➞ False
Notes
The empty set and the set itself are both valid subsets of a set (we are not talking about proper subsets here).
The set and the subset will each have unique elements.
"""

def validate_subsets(subsets, my_set):

    return all(set(x).issubset(my_set) for x in subsets)


    # for sub in subsets:
    #     for num in sub:
    #         if num not in my_set:
    #             return False
    #             break
    # return True


    # merged_subset = []
    # for subset in subsets:
    #     merged_subset.extend(subset)
    #
    # return set(list(set(merged_subset))) == set(my_set)
    #
    # # return set(merged_subset).issubset(set(my_set))

print(validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]))
print(validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]))
print(validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]))
print(validate_subsets([[1, 2, 3, 4]], [1, 2, 3]))
print(validate_subsets([['a', 'b'], ['b', 'c'], ['a', 'c']], ['a', 'b', 'c']))
print(validate_subsets([[True, False], [True]], [True, False]))
print(validate_subsets([[True], [True, False]], [True]))