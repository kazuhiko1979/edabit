"""
Day Number of Year
Each year has 365 or 366 days. Given a string date representing a Gregorian calendar date formatted as month/day/year, return the day-number of the year.

Examples
day_of_year("11/16/2020") ➞ 321

day_of_year("1/9/2019") ➞ 9

day_of_year("3/1/2004") ➞ 61

day_of_year("12/31/2000") ➞ 366
Notes
All input strings in tests are valid dates.
"""



# v1
# import datetime
#
#
# def day_of_year(date):
#
# 	d1 = datetime.datetime.strptime(date, '%m/%d/%Y')
# 	d0 = d1.replace(d1.year, month=1, day=1)
# 	return (d1 - d0).days + 1


print(day_of_year("11/16/2020"))
print(day_of_year("1/9/2019"))
print(day_of_year("3/1/2004"))
print(day_of_year("12/31/2000"))





