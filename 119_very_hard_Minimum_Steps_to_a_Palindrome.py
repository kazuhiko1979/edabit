"""
Minimum Steps to a Palindrome
Given an incomplete palindrome as a string, return the minimum letters needed to be added on to the end to make the string a palindrome.

Examples
min_palindrome_steps("race") ➞ 3
# Add 3 letters: "car" to make "racecar"

min_palindrome_steps("mada") ➞ 1
# Add 1 letter: "m" to make "madam"

min_palindrome_steps("mirror") ➞ 3
# Add 3 letters: "rim" to make "mirrorrim"
Notes
Trivially, words which are already palindromes should return 0.
"""


def min_palindrome_steps(txt):

    for i in range(len(txt)):
        if txt[i:] == txt[i:][::-1]:
            return i

        # count = 0
        # temp = ""
        # if txt == txt[::-1]:
        #     return count
        # for i in txt:
        #     temp += i
        #     temp = temp[::-1]
        #     result = txt + temp
        #     count += 1
        #     if result == result[::-1]:
        #         return count
        #     else:
        #         temp = temp[::-1]


print(min_palindrome_steps("race"))
print(min_palindrome_steps("mada"))
print(min_palindrome_steps("mirror"))
print(min_palindrome_steps("maa"))
print(min_palindrome_steps("m"))
print(min_palindrome_steps("rad"))
print(min_palindrome_steps("madam"))
print(min_palindrome_steps("radar"))
print(min_palindrome_steps("www"))
print(min_palindrome_steps("me"))
print(min_palindrome_steps("rorr"))
print(min_palindrome_steps("pole"))
