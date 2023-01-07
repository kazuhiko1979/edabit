"""
When to Sleep?
Given a series of lists, with each individual list containing the time of the alarm set and the sleep duration, return what time to sleep.

Examples
bed_time(["07:50", "07:50"]) ➞ ["00:00"]
# The second argument means 7 hours, 50 minutes sleep duration.

bed_time(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]) ➞ ["20:15", "22:00", "23:30"]
# The second argument of each sub list means 10 hours sleep duration.

bed_time(["05:45", "04:00"], ["07:10", "04:30"]) ➞ ["01:45", "02:40"]
# Sleep duration can be different among the lists.
Notes
Times should be given in 24-hrs (i.e. "23:25" as opposed to "11:25PM").
Return a list of strings.
"""
from datetime import datetime, timedelta

# v2
def bed_time(*times):

	res = []
	for wake, duration in times:
		h = int(wake[:2]) - int(duration[:2])
		s = int(wake[-2:]) - int(duration[-2:])
		res.append('{:02}:{:02}'.format((h-1) % 24 if s < 0 else h % 24, s % 60))
	return res



# v1
# def bed_time(*times):
#
# 	result = []
#
# 	for i in times:
#
# 		dt1_alart_h = int(i[0][:2])
# 		dt1_alart_m = int(i[0][3:])
# 		dt2_alart_h = int(i[1][:2])
# 		dt2_alart_m = int(i[1][3:])
#
# 		dt1 = datetime(year=2019, month=1, day=1, hour=dt1_alart_h, minute=dt1_alart_m)
# 		dt2 = datetime(year=2018, month=12, day=31, hour=dt2_alart_h, minute=dt2_alart_m)
#
# 		td = dt1 - dt2
#
# 		if td.days == 0:
# 			td = str(datetime.strptime(str(td), '%H:%M:%S'))[-8:-3]
# 			result.append(td)
# 		elif td.days == 1:
# 			td = td - timedelta(days=1)
# 			td = str(datetime.strptime(str(td), '%H:%M:%S'))[-8:-3]
# 			result.append(td)
# 	return result

print(bed_time(['07:50', '07:50']))
print(bed_time(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]))
print(bed_time(["05:45", "04:00"], ["07:10", "04:30"]))
