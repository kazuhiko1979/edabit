"""
In this challenge, sort an array containing a series of dates given as strings. Each date is given in the format DD-MM-YYYY_HH:MM:

"12-02-2012_13:44"
The priority of criteria used for sorting will be:

Year
Month
Day
Hours
Minutes
Given an array arr and a string type, implement a function that returns:

if type is equal to "ASC", the array arr sorted in ascending order.
if type is equal to "DSC", the array arr sorted in descending order.
Examples
sortDates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") ➞ [
  "10-02-2016_12:30", "10-02-2018_12:15", "10-02-2018_12:30"
]

sortDates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") ➞ [
  "10-02-2018_12:30", "10-02-2018_12:15", "10-02-2016_12:30"
]

sortDates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") ➞ [
  "01-01-1999_00:55", "09-02-2000_10:03", "10-02-2000_18:29"
]
Notes
Remember: the date is in the format DD-MM-YYYY_HH:MM.
"""


import datetime

def sort_dates(tuplelist, txt):

    dtList = []

    for tuple in tuplelist:

        dt = datetime.datetime.strptime(tuple, "%d-%m-%Y_%H:%M")
        dtList.append(dt)

    if txt == "ASC":
        sorted_dtlist = sorted(dtList, reverse=False)
        return [i.strftime("%d-%m-%Y_%H:%M") for i in sorted_dtlist]

    if txt == "DSC":
        sorted_dtlist = sorted(dtList, reverse=True)
        return [i.strftime("%d-%m-%Y_%H:%M") for i in sorted_dtlist]


print(sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC"))
print(sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC"))
print(sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC"))