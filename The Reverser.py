"""
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

Examples
reverse("Hello World") ➞ "DLROw OLLEh"
reverse("ReVeRsE") ➞ "eSrEvEr"
reverse("Radar") ➞ "RADAr"
"""

def reverse(txt):
    # txt = list(reversed(txt))
    # txt =  ''.join(txt)
    # txt = txt.swapcase()
    # return txt

    # return txt.swapcase()[::-1]
    return txt[::-1].swapcase()


print(reverse("Hello World"))
print(reverse("ReVeRsE"))
print(reverse("Radar"))
