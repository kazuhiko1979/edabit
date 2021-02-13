"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.

Examples
is_valid_PIN("1234") ➞ True
is_valid_PIN("12345") ➞ False
is_valid_PIN("a234") ➞ False
is_valid_PIN("") ➞ False
"""
def is_valid_PIN(pin):

    # print(len(pin))

    if len(pin) == 4 or (len(pin) == 6):
        if pin.isdigit():
            return True
    return False

print(is_valid_PIN("1234"))
print(is_valid_PIN("12345"))
print(is_valid_PIN("a234"))
print(is_valid_PIN(""))

