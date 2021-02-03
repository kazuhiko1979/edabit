"""
Create a function that takes a string and returns a string
in which each character is repeated once.

Examples
double_char("String") ➞ "SSttrriinngg"
double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"
double_char("1234!_ ") ➞ "11223344!!__  "
"""
def double_char(txt):

    n = 2
    char = ''.join([char*n for char in txt])
    return char

print(double_char("String"))
