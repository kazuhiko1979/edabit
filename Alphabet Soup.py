"""
Create a function that takes a string and returns a string with its letters in alphabetical order.

Examples
alphabet_soup("hello") ➞ "ehllo"
alphabet_soup("edabit") ➞ "abdeit"
alphabet_soup("hacker") ➞ "acehkr"
alphabet_soup("geek") ➞ "eegk"
alphabet_soup("javascript") ➞ "aacijprstv"
"""
def alphabet_soup(txt):

    return ''.join(sorted(txt))


print(alphabet_soup("hello"))
print(alphabet_soup("edabit"))
print(alphabet_soup("hacker"))