"""
Create a function that determines whether a string is a valid hex code.

A hex code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit from 0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase.

Examples
is_valid_hex_code("#CD5C5C") ➞ True

is_valid_hex_code("#EAECEE") ➞ True

is_valid_hex_code("#eaecee") ➞ True

is_valid_hex_code("#CD5C58C") ➞ False
# Length exceeds 6

is_valid_hex_code("#CD5C5Z") ➞ False
# Not all alphabetic characters in A-F

is_valid_hex_code("#CD5C&C") ➞ False
# Contains unacceptable character

is_valid_hex_code("CD5C5C") ➞ False
# Missing #
"""


def is_valid_hex_code(txt):

    hex_digits = set("0123456789abcdef")

    if txt[0] == '#' and len(txt[1:].lower()) == 6:
        for char in txt[1:].lower():
            if not (char in hex_digits):
                return False
        return True
    return False

print(is_valid_hex_code("#CD5C5C"))
print(is_valid_hex_code("#CD5C58C"))
print(is_valid_hex_code("#CD5C&C"))
print(is_valid_hex_code("#eaecee"))