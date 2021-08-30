"""
A palindrome is a series of letters or numbers that reads equivocally backwards. Write a recursive function that determines whether a given string is a palindrome or not.

Examples
is_palindrome("Go hang a salami, I'm a lasagna hog!") ➞ True

is_palindrome("This phrase, surely, is not a palindrome!") ➞ False

is_palindrome("Eva, can I see bees in a cave?") ➞ True
Notes
Symbols and special characters should be ignored.
You are expected to solve this challenge via recursion.
"""
import re


def is_palindrome(p):

    p = re.sub("\W+", "", p).lower()
    p_reversed = p[::-1]

    return is_palindromeHelper(p, p_reversed)

def is_palindromeHelper(p, p_reversed):

    return p == p_reversed



print(is_palindrome("Go hang a salami, I'm a lasagna hog!"))
print(is_palindrome("This phrase, surely, is not a palindrome!"))
print(is_palindrome("Eva, can I see bees in a cave?"))