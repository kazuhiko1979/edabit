"""
Write a method that when passed a date as "dd mm yyyy" and returns the date's weekday name in the Dutch culture.

Examples
weekday_dutch("21 9 1970") ➞ "maandag"

weekday_dutch(new DateTime("2 9 1945") ➞ "zondag"

weekday_dutch(new DateTime("9 11 2001") ➞ "dinsdag"
"""
import calendar


def weekday_dutch(date):
    dic = {
        "Monday": "maandag",
        "Tuesday": "dinsdag",
        "Wednesday": "woensdag",
        "Thursday": "donderdag",
        "Friday": "vrijdag",
        "Saturday": "zaterdag",
        "Sunday": "zondag"
    }

    day, month, year = [int(i) for i in date.split(' ')]
    dayNumber = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]

    day_of_week = days[dayNumber]
    for i in dic:
        if i == day_of_week:
            return dic.get(i)

print(weekday_dutch("21 9 1970"))
print(weekday_dutch("22 9 1970"))
print(weekday_dutch("23 9 1970"))
print(weekday_dutch("24 9 1970"))
print(weekday_dutch("25 9 1970"))
print(weekday_dutch("26 9 1970"))
print(weekday_dutch("27 9 1970"))
print(weekday_dutch("10 12 2050"))
print(weekday_dutch("14 10 6010"))
print(weekday_dutch("31 1 1000"))
print(weekday_dutch("8 12 2112"))
print(weekday_dutch("12 12 1212"))



