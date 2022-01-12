"""
Unlucky Years
Create a function which returns how many Friday 13ths there are in a given year.

Examples
how_unlucky(2020) ➞ 2

how_unlucky(2026) ➞ 3

how_unlucky(2016) ➞ 1
"""

from datetime import date
import datetime
import calendar

def how_unlucky(year):

    return sum(date(year, m, 13).strftime('%A') == 'Friday' for m in range(1, 13))
    

    # count = 0
    # for month in range(1, 13):
    #
    #     x = datetime.datetime(year, month, 13)
    #     if x.strftime("%A") == "Friday":
    #         count += 1
    #
    # return count

print(how_unlucky(2000))
print(how_unlucky(2001))
print(how_unlucky(2002))
print(how_unlucky(2003))
print(how_unlucky(2004))
print(how_unlucky(2005))
print(how_unlucky(2006))
print(how_unlucky(2007))
print(how_unlucky(2008))
print(how_unlucky(2009))
print(how_unlucky(2010))


# print(how_unlucky(2020))
# print(how_unlucky(2026))
# print(how_unlucky(2016))

