"""
A Week Later
Create a function which takes in a date as a string, and returns the date a week after.

Examples
week_after("12/03/2020") ➞ "19/03/2020"

week_after("21/12/1989") ➞ "28/12/1989"

week_after("01/01/2000") ➞ "08/01/2000"
"""

import datetime

def week_after(d):

    # v2
    # date = datetime.datetime.strptime(d, "%d/%m/%Y") + datetime.timedelta(days=7)
    # return date.strftime("%d/%m/%Y")

    # v1
    d = datetime.datetime.strptime(d, "%d/%m/%Y")
    week = datetime.timedelta(days=7)

    d = d + week
    return d.strftime("%d/%m/%Y")

print(week_after("12/03/2020"))
print(week_after("28/12/2020"))


