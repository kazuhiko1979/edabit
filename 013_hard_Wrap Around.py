"""
Create a function to reproduce the wrap around effect shown:

Examples
wrap_around("Hello, World!", 2) ➞ "llo, World!He"

wrap_around("From what I gathered", -4) ➞ "eredFrom what I gath"

wrap_around("Excelsior", 30) ➞ "elsiorExc"

wrap_around("Nonscience", -116) ➞ "cienceNons"
Notes
The offset can be negative.
The offset can be greater than the length of string.
"""
def wrap_around(string, offset):

    return string[offset % len(string):] + string[:offset % len(string)]

    # lensOfString = len(string)
    # minusOfOffset = 0
    #
    # if offset < 0:
    #     minusOfOffset = -offset
    # else:
    #     offset = offset
    #
    # # 絶対値判断:
    # while abs(offset) >= lensOfString:
    #     offset = abs(offset) - lensOfString
    #
    # if not minusOfOffset:
    #     deleteInString = string[:offset]
    #     string = string + deleteInString
    #     return string[len(deleteInString):]
    # else:
    #     if offset > 0:
    #         offset = -offset
    #     deleteInString = string[offset:]
    #     string = deleteInString + string
    #     return string[:-len(deleteInString)]

print(wrap_around("Hello, World!", 2))
print(wrap_around("From what I gathered", -4))
print(wrap_around("No Changes", 0))
print(wrap_around("S", -60))
print(wrap_around("Subordinating", 2))
print(wrap_around("Assemblywomen", -6))
print(wrap_around("Pedantic", 4))
print(wrap_around("Nonscience", -116))
print(wrap_around("Excelsior", 30))
print(wrap_around("Incomprehensibilities", 50))


