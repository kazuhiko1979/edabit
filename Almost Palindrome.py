"""
A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function that returns True if a string is an almost-palindrome and False otherwise.

Examples
almost_palindrome("abcdcbg") ➞ True
# Transformed to "abcdcba" by changing "g" to "a".

almost_palindrome("abccia") ➞ True
# Transformed to "abccba" by changing "i" to "b".

almost_palindrome("abcdaaa") ➞ False
# Can't be transformed to a palindrome in exactly 1 turn.

almost_palindrome("1234312") ➞ False
Notes
Return False if the string is already a palindrome.

"""

# txt = "abcdcbg"
# txt = "abccia"
# txt = "abcdaaa"
# # # txt = "abccia"
# txt = "1234312"
# txt = "gggffff"
# txt = "gggfggg"


def almost_palindrome(txt):

    reversed_txt = ''.join(list(reversed(txt)))
    return len([i for i in range(len(txt)) if txt[i] != reversed_txt[i]]) == 2


print(almost_palindrome("abcdcbg"))
print(almost_palindrome("abccia"))
print(almost_palindrome("abcdaaa"))
print(almost_palindrome("gggfgig"))
print(almost_palindrome("gggffff"))
print(almost_palindrome("ggggg"))
print(almost_palindrome("gggfggg"))


