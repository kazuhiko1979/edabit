"""
Valid Division
Create a function that takes a division equation d and checks if it will return a whole number without decimals after dividing.

Examples
valid_division("6/3") ➞ True

valid_division("30/25") ➞ False

valid_division("0/3") ➞ True
Notes
Return "invalid" if division by zero.
"""

def valid_division(d):

    p, q = [int(x)for x in d.split('/')]
    return not (p&q) if q else 'invalid'


    # try:
    #     return eval(d).is_integer()
    # except:
    #     return 'invalid'



    # try:
    #     divided = int(d.split('/')[0]) / int(d.split('/')[1])
    #     return divided.is_integer()
    # except:
    #     return 'invalid'


print(valid_division("6/3"))
print(valid_division("30/25"))
print(valid_division("0/3"))
print(valid_division("13/12"))
print(valid_division("0/0"))