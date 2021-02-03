"""
Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

Return cdea boolean value (True or False).
Return True if the amount of x's and o's are the same.
Return False if they aren't the same amount.
The string can contain any character.
When "x" and "o" are not in the string, return True.
Examples
XO("ooxx") ➞ True
XO("xooxx") ➞ False
XO("ooxXm") ➞ True
# Case insensitive.
XO("zpzpzpp") ➞ True
# Returns True if no x and o.
XO("zzoo") ➞ False
"""
def XO(txt):

    txt = txt.lower()
    str_o = "o"
    str_x = "x"
    num_o = txt.count(str_o)
    num_x = txt.count(str_x)
    if num_x == num_o:
        return True
    return False

    if str_o and str_x not in txt:
        return True


print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
# Case insensitive.
print(XO("zpzpzpp"))
# Returns True if no x and o.
print(XO("zzoo"))














