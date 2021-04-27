"""
You are given three inputs: a string, one letter, and a second letter.

Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.

Examples
first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
# Every instance of "a" occurs before every instance of "j".

first_before_second("knaves knew about waterfalls", "k", "w") ➞  True

first_before_second("happy birthday", "a", "y") ➞ False
# The "a" in "birthday" occurs after the "y" in "happy".

first_before_second("precarious kangaroos", "k", "a") ➞ False
Notes
All strings will be in lower case.
All strings will contain the first and second letters at least once.
"""


def first_before_second(s, first, second):

    #
    # first_delete_num = s.find(first)
    # first_delete_num = first_delete_num + 1
    # s = s[first_delete_num:]
    #
    # if s.find(first) < s.find(second):
    #     return True
    # else:
    #     return False
    # print(s.rindex(first))
    # print(s.index(second))
    return s.rindex(first) < s.index(second)

print(first_before_second("a rabbit jumps joyfully", "a", "j"))
print(first_before_second("knave knew about waterfalls", "k", "w"))
print(first_before_second("maria makes money", "m", "o"))
print(first_before_second("the hostess made pecan pie", "h", "p"))
print(first_before_second("barry the butterfly flew away", "b", "f"))
print(first_before_second("happy birthday", "a", "y"))
print(first_before_second("taken by the beautiful sunrise", "u", "s"))
print(first_before_second("moody muggles", "m", "o"))

