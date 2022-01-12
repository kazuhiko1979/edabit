"""
Sum of v0w3ls
Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.

Vowel	Number
A	4
E	3
I	1
O	0
U	0
Examples
sum_of_vowels("Let\'s test this function.") ➞ 8

sum_of_vowels("Do I get the correct output?") ➞ 10

sum_of_vowels("I love edabit!") ➞ 12
Notes
Vowels are case-insensitive (e.g. A = 4 and a = 4).
"""

def sum_of_vowels(str):

    txt = str.lower()
    return 4 * txt.count('a') + 3 * txt.count('e') + txt.count('i')

    # v = {'a': 4, 'e': 3, 'i': 1}
    # return sum([v[i] for i in str.lower() if i in v])


    # count = 0
    #
    # for i in str:
    #     if i.lower() == 'a':
    #         count += 4
    #     elif i.lower() == 'e':
    #         count += 3
    #     elif i.lower() == 'i':
    #         count += 1
    # return count

print(sum_of_vowels("Let\'s test this function."))
print(sum_of_vowels("Do I get the correct output?"))
print(sum_of_vowels("I love edabit!"))