"""
Recursion: Count Vowels
Write a function that recursively returns the number of vowels in a string.

If it wasn't clear enough already, you should use recursion in your solution.

Examples
vowels("apple") ➞ 2

vowels("cheesecake") ➞ 5

vowels("bbb") ➞ 0

vowels("") ➞ 0
Notes
Recursive functions call themselves.
All letters will be in lower case.
For this challenge, the vowels are a, e, i, o, and u.
"""

def vowels(string):

    # v2
    return 0 if not string else (string[0] in 'aiueo') + vowels(string[1:])


    # v1.5
    # if len(string) == 0:
    #     return 0
    # if string[0] in 'aiuoe':
    #     return 1 + vowels(string[1:])
    # else:
    #     return vowels(string[1:])


    # v1
    # if len(string) > 0:
    #     if string[0] in "aiueo":
    #         return vowels(string[1:]) + 1
    #     else:
    #         return vowels(string[1:])
    # return 0

print(vowels("apple"))
print(vowels("cheesecake"))
print(vowels("bbb"))
print(vowels(""))
