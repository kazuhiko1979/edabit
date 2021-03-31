import datetime as dt
import calendar

def main():

    # print(dt.date.today())
    # print(dt.date.today().year)
    # print(dt.date.today().month)
    # print(dt.date.today().day)
    # print(dt.date.today().weekday())
    # print(dt.date.today().ctime())
    # print(dt.date.today().strftime("%y/%m/%d"))
    # print(dt.date.today().strftime("%Y/%m/%d"))
    # print(dt.date.today().isoformat())

    # print(dt.date.today().replace(day=1))
    # range = calendar.monthrange(
    #     dt.date.today().year,
    #     dt.date.today().month
    # )
    # # print(range)
    # print(dt.date.today().replace(day=range[1]))

    # print(dt.datetime.now())
    # print(dt.datetime.now().year)
    # print(dt.datetime.now().month)
    # print(dt.datetime.now().day)
    # print(dt.datetime.now().hour)
    # print(dt.datetime.now().minute)
    # print(dt.datetime.now().second)
    # print(dt.datetime.now().microsecond)

    # now = dt.datetime.now()
    # print(now+dt.timedelta(seconds=1))
    # print(now+dt.timedelta(minutes=1))
    # print(now+dt.timedelta(hours=1))
    # print(now+dt.timedelta(days=1))
    # print(now+dt.timedelta(weeks=1))

    # print(dt.datetime.strptime('2021/03/27', '%Y/%m/%d'))
    # print(dt.datetime.strptime('2021.03.27', '%Y.%m.%d'))
    # print(dt.datetime.strptime('2021 03 27', '%Y %m %d'))
    # print(dt.datetime.strptime('20210327', '%Y%m%d'))
    # print(dt.datetime.strptime('2021 03 27 15:57:55', '%Y %m %d %H:%M:%S'))

    print(dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(dt.datetime.now().strftime("%Y%m%d %H%M%S"))

    return

if __name__ == '__main__':
    main()
