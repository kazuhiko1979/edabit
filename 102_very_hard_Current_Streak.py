from datetime import datetime
from dateutil.relativedelta import relativedelta


def total_days_between_dates(date1, date2):

	date1 = datetime.strptime(date1, '%Y-%m-%d')
	date2 = datetime.strptime(date2, '%Y-%m-%d')

	delta = relativedelta(date2, date1)
	total_days = delta.years * 365 + delta.days

	return total_days

def current_streak(today, lst):
	result = []
	for a, b in zip(lst, lst[1:]):
		diff_days = total_days_between_dates(a['date'], b['date'])
		result.append(diff_days)

	start = 1
	for i in result:
		start = (start + 1) if i == 1 else 1

	return start if lst and total_days_between_dates( today, lst[-1]['date']) == 0 else 0


print(current_streak("1985-03-19", [
  {
    "date": "1985-03-19"
  }
]))

print(current_streak("2019-09-23", [
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]))

print(current_streak("2019-09-30", [
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-20"
  },
  {
    "date": "2019-09-26"
  },
  {
    "date": "2019-09-27"
  },
  {
    "date": "2019-09-30"
  }
]))

print(current_streak("2019-09-23", [
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-20"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]))

print(current_streak("2019-09-23", [
  {
    "date": "2019-06-25"
  },
  {
    "date": "2019-06-28"
  },
  {
    "date": "2019-07-02"
  },
  {
    "date": "2019-07-07"
  },
  {
    "date": "2019-07-09"
  },
  {
    "date": "2019-07-12"
  },
  {
    "date": "2019-07-13"
  },
  {
    "date": "2019-07-14"
  },
  {
    "date": "2019-07-15"
  },
  {
    "date": "2019-07-16"
  },
  {
    "date": "2019-07-17"
  },
  {
    "date": "2019-07-25"
  },
  {
    "date": "2019-07-26"
  },
  {
    "date": "2019-07-29"
  },
  {
    "date": "2019-07-31"
  },
  {
    "date": "2019-08-03"
  },
  {
    "date": "2019-08-06"
  },
  {
    "date": "2019-08-07"
  },
  {
    "date": "2019-08-09"
  },
  {
    "date": "2019-08-12"
  },
  {
    "date": "2019-08-13"
  },
  {
    "date": "2019-08-14"
  },
  {
    "date": "2019-08-16"
  },
  {
    "date": "2019-08-17"
  },
  {
    "date": "2019-08-21"
  },
  {
    "date": "2019-08-22"
  },
  {
    "date": "2019-08-23"
  },
  {
    "date": "2019-08-24"
  },
  {
    "date": "2019-08-25"
  },
  {
    "date": "2019-08-26"
  },
  {
    "date": "2019-08-27"
  },
  {
    "date": "2019-08-28"
  },
  {
    "date": "2019-08-29"
  },
  {
    "date": "2019-08-30"
  },
  {
    "date": "2019-09-02"
  },
  {
    "date": "2019-09-03"
  },
  {
    "date": "2019-09-04"
  },
  {
    "date": "2019-09-05"
  },
  {
    "date": "2019-09-06"
  },
  {
    "date": "2019-09-08"
  },
  {
    "date": "2019-09-11"
  },
  {
    "date": "2019-09-12"
  },
  {
    "date": "2019-09-13"
  },
  {
    "date": "2019-09-15"
  },
  {
    "date": "2019-09-16"
  },
  {
    "date": "2019-09-17"
  },
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-20"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]))

print(current_streak("2019-09-25", [
  {
    "date": "2019-09-16"
  },
  {
    "date": "2019-09-17"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]))

print(current_streak("2019-09-16", []))