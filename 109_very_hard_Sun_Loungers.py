"""
Sun Loungers
A long stretch of beach is represented by a string of two characters 0 - free, 1 - occupied. Due to recent restrictions, a new person cannot take place next to another. There has to be one free place between two people lounging on the beach. Create a function to compute how many new people at most can settle in on the given beach.

Examples
sun_loungers("10001") ➞ 1
# Can take place in the middle.

sun_loungers("00101") ➞ 1
# Can take place on the left.

sun_loungers("0") ➞ 1
# Can take one place.

sun_loungers("000") ➞ 2
# Can take places on the left and on the right.
"""
def sun_loungers(beach):
	return sum([(len(i)-1)//2 for i in '0{}0'.format(beach).split('1')])


# def sun_loungers(beach):
#
# 	count = 0
#
# 	if beach == '0':
# 		return 1
#
# 	if beach.startswith("00"):
# 		beach = '1' + beach[1:]
# 		count += 1
# 	if beach.endswith("00"):
# 		beach = beach[:-1] + "1"
# 		count += 1
# 	i = 1
# 	while i < len(beach) - 1:
# 		if beach[i] == "0" and beach[i - 1:i + 2] == "000":
# 			count += 1
# 			beach = beach[:i] + "1" + beach[i + 1:]
# 		i += 1
# 	return count


# if beach[0] == '0' and beach[1] == '0':
	# 	beach = '1' + beach[1:]
	# 	count += 1
	# if beach[-1] == '0' and beach[-2] == '0':
	# 	beach = beach[:-1] + '1'
	# 	count += 1

	# for i in range(0, len(beach)):
	# 	if beach[i] == '0':
	# 		if beach[i+1] == '0' and beach[i-1] == '0':
	# 			beach = beach[:i] + "1" + beach[i+1:]
	# 			count += 1
	# return count


print(sun_loungers("10001"))
print(sun_loungers("00101"))
print(sun_loungers("0"))
#
print(sun_loungers("000"))
#
print(sun_loungers("001000100000001010001010010000001000101000000"))
# print(sun_loungers("010000100000000010010000001010000000010100001000000010010000000001000000001000000010000000100100000000100000100100010000001"))
# print(sun_loungers("10001000000100000010000001000100000001010000001000100010010000000010000010001000000010010010000000001001001000000010000000100000001010000000100000000010000000100010000010000010000001000100001001001000000100000010000010100000001000000000"))
# print(sun_loungers("00100100100000100100000001000001000001010000010000000100000010001001000100000001001000001010000001000010100001000010000000010010000000100100000100000000100100000100000000100010001000010000001001000000001000100000100000001000100100000010000000010000100000001000100001010000000100000100000001000100000000101001000001000000010100000010000010000000100000000100100100000001010010000010100100010000000010010000001000010000010000100000"))


