import pytz
import datetime as dt

from datetime import timezone
from dateutil import parser as par

def main():

    # print(dt.datetime.now())
    # print(dt.datetime(2018, 11, 28, 3, 30))
    # print(dt.datetime.utcnow())

    # タイムゾーン情報
    local_time_tz = pytz.timezone('Asia/Tokyo')
    # print(local_time_tz.localize(dt.datetime.now()))

    # London
    print(dt.datetime.now(tz=timezone.utc))
    # Tokyo
    print(dt.datetime.now(tz=local_time_tz))
    #
    print(dt.datetime.now().astimezone(local_time_tz))

    utc_str = "Sat Nov 24 16:27:57 +0000 2018" # London
    jst_time = par.parse(utc_str).astimezone(pytz.timezone('Asia/Tokyo'))
    print(jst_time)

    return

if __name__ == '__main__':
    main()

