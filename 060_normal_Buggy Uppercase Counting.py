"""
In the Code tab is a function which is meant to return how many uppercase letters there are in a list of various words. Fix the list comprehension so that the code functions normally!

Examples
count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6

count_uppercase(["little", "lower", "down"]) ➞ 0

count_uppercase(["EDAbit", "Educate", "Coding"]) ➞ 5
"""

def count_uppercase(lst):

    return sum([letter.isupper() for word in lst for letter in word])

    # count = 0
    # for i in ''.join(lst):
    #     if i.isupper():
    #         count += 1
    # return count


print(count_uppercase(["SOLO", "hello", "Tea", "wHat"]))
print(count_uppercase(["little", "lower", "down"]))
print(count_uppercase(["EDAbit", "Educate", "Coding"]))