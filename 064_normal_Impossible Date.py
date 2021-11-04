"""
Given the parameters day, month and year, return whether that date is a valid date.

Examples
is_valid_date(35, 2, 2020) ➞ False
# February doesn't have 35 days.

is_valid_date(8, 3, 2020) ➞ True
# 8th March 2020 is a real date.

is_valid_date(31, 6, 1980) ➞ False
# June only has 30 days.
Notes
Try using the datetime module to complete this challenge (see the Resources tab for some tutorials on this).
import math
"""
import datetime

def is_valid_date(d, m, y):

    try:
        return bool(datetime.datetime(year=y, month=m, day=d))
    except:
        return False

    # isValidDate = True
    #
    # try:
    #     datetime.datetime(y, m, d)
    # except ValueError:
    #     isValidDate = False
    #
    # if isValidDate:
    #     return True
    # else:
    #     return False


print(is_valid_date(35, 2, 2020))
print(is_valid_date(8, 3, 2020))
print(is_valid_date(31, 6, 1980))







