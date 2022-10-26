"""
Snail Crawl out of the Bucket
A snail fell into a bucket and wanted to crawl out. Assuming we already know the snail can climb 5cm per minute, the snail can crawl for 30 minutes continuously and then needs to rest for 10 minutes. When it is resting it will slide down 30cm.

How many minutes will it take for the snail to crawl out from different depths? Create a function that takes the bucket depth (the unit is cm) as an argument and returns the time in minutes.

if depth = 270
the snail crawling process
process: (150 - 30) +  150
minutes: (30+10) + 150 / 5
it will take 70 minutes
the last 150cm, the snail doesn't need a rest
Examples
cal(31) ➞ 7

cal(150) ➞ 30

cal(200) ➞ 56
Notes
The depth is a positive integer.
If the time is less than one minute it still counts as one minute.
"""
import math

def cal(depth):
	
	if depth <= 150:
		return math.ceil(depth / 5)
	else:
		return math.ceil((depth + depth // 150 * 30) / 5 + 10 * (depth // 150))


# v2
# def cal(depth):
#
# 	minutes = 0
# 	count = 0
# 	climb = 0
#
# 	while climb < depth:
# 		climb += 5
# 		count += 1
# 		minutes += 1
# 		if count > 30:
# 			count = 0
# 			climb -= 30
# 			minutes += 10
# 	return minutes




# v1
# def cal(depth):
#
# 	climb = 5
# 	minutes = 0
# 	temp_minutes = 0
# 	length = 0
# 	while depth >= 0:
# 		minutes += 1
# 		temp_minutes += 1
# 		length = climb * minutes
# 		depth -= climb
# 		if depth != 0:
# 			if temp_minutes % 30 == 0:
# 				length -= 30
# 				depth += 30
# 				minutes += 10
# 				temp_minutes = 0
# 		else:
# 			return minutes
# 	return minutes

print(cal(31))
print(cal(150))
print(cal(200))
print(cal(15))
print(cal(151))
print(cal(160))
print(cal(300))







