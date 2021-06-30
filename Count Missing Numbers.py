"""
Create a function that takes a list of "mostly" numbers, counts the amount of missing numbers and returns their sum. Watch out for strings!

Examples
count_missing_nums(["1", "3", "5", "7", "9"]) ➞ 4
# 1+1+1+1

count_missing_nums(["7", "3", "1", "9", "5"]) ➞ 4

count_missing_nums(["1", "5", "B", "9", "z"]) ➞ 6
Notes
The data might be dirty! Clean out any filthy strings.
"""

def count_missing_nums(lst):

    is_num_list = sorted([int(i) for i in lst if i.isnumeric()])
    master_list = ([j for j in range(int(is_num_list[0]), int(is_num_list[-1])+1)])

    return len(set(master_list) - set(is_num_list))

print(count_missing_nums(["1", "3", "5", "7", "9"]))
print(count_missing_nums(["1", "5", "B", "9", "z"]))
print(count_missing_nums(["7", "3", "1", "9", "5"]))




