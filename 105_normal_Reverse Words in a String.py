"""
Reverse Words in a String
Given an input string, reverse the string word by word.

Examples
reverse_words("the sky is blue") ➞ "blue is sky the"

reverse_words("  hello world!  ") ➞ "world! hello"

reverse_words("a good   example") ➞ "example good a"
Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
Try to solve this in linear time.
"""

def reverse_words(str):

    return ' '.join([i for i in reversed(str.split())])

print(reverse_words("the sky is blue"))
print(reverse_words("  hello world!  "))




