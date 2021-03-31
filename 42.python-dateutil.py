from dateutil.relativedelta import relativedelta
from datetime import date
from dateutil import rrule

import datetime as dt
import calendar as cal


def main():

    # print('Test')
    # # print(date(2021, 3, 27)+relativedelta(day=1))
    # # print(date(2021, 2, 27) + relativedelta(day=31))
    # # print(date(2021, 3, 31)+
    # #       relativedelta(weekday=cal.TUESDAY))
    #
    # # birthdate = date(1979, 10,24)
    # # print(relativedelta(
    # #     dt.date.today(), birthdate).years)
    #
    # 11月の営業日を取得する
    business_days = rrule.rrule(rrule.WEEKLY,
            byweekday = (cal.MONDAY, cal.THURSDAY, cal.WEDNESDAY,
                         cal.THURSDAY, cal.FRIDAY),
            dtstart   = dt.datetime(2108, 11, 1),
            until      = dt.datetime(2018, 11, 30))

    print(business_days)

    # for i in business_days:
    #     print(i)

if __name__ == '__main__':
    main()