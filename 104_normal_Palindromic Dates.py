"""
Palindromic Dates
The 2nd of February 2020 is a palindromic date in both dd/mm/yyyy and mm/dd/yyyy format (02/02/2020). Given a date in dd/mm/yyyy format, return True if the date is palindromic in both date formats, otherwise return False.

Examples
palindromic_date("02/02/2020") ➞ True

palindromic_date("11/12/2019") ➞ False

palindromic_date("11/02/2011") ➞ False
# Although 11/02/2011 is palindromic in dd/mm/yyyy format,
# it isn't in mm/dd/yyyy format (02/11/2011)
Notes
All dates will be valid in both date formats.
The date must be palindromic in both dd/mm/yyyy and mm/dd/yyyy formats to pass.
"""
import datetime

def palindromic_date(date):

    d, m, y = date.split('/')
    # print(d, m, y)
    return (d+m)[::-1] == y and (m+d)[::-1] == y

    # date = date.split('/')
    # dt = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
    # year = ''.join(list(reversed(date[2])))
    # return dt.month == dt.day and (date[1] + date[0]) == year

print(palindromic_date("02/02/2020"))
print(palindromic_date("12/12/2121"))
print(palindromic_date("03/11/3369"))
print(palindromic_date("11/03/2775"))
print(palindromic_date("03/03/1822"))