"""
Recursion: String Palindromes
Write a function that recursively determines if a string is a palindrome.

Examples
is_palindrome("abcba") ➞ True

is_palindrome("b") ➞ True

is_palindrome("") ➞ True

is_palindrome("ad") ➞ False
Notes
An empty string counts as a palindrome.
"""

def is_palindrome(word):

    if len(word) > 0:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        return False
    return True


print(is_palindrome("abcba"))
print(is_palindrome("abbba"))
print(is_palindrome("abbbba"))
print(is_palindrome("b"))
print(is_palindrome(""))
print(is_palindrome("ad"))