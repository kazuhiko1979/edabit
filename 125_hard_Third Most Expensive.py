"""
Burglary Series (05): Third Most Expensive
Time to call your lover to inform him/her what he/she lost in the burglary.

Given a dictionary of the stolen objects, return the 3rd most expensive item on the list. If that is not possible, because there are not enough items, return False.

Examples
third_most_expensive({}) ➞ False
# Items are less than three.

third_most_expensive({"piano": 100, "stereo": 200 }) ➞ False
# Items are less than three.

third_most_expensive({"piano": 100, "stereo": 200, "tv": 10, "timmy": 500 }) ➞  "piano"
# 'piano' is the third most expensive item.
Notes
All prices will be of different monetary values.
"""
import operator

def third_most_expensive(dct):

	# v3
	return sorted(dct.items(), key=operator.itemgetter(1), reverse=True)[2][0] if len(dct) > 2 else False

	# v2
	#
	# if len(dct) > 2:
	# 	sorted_dct = sorted(dct.items(), key=lambda kv: kv[1], reverse=True)[2]
	# 	return sorted_dct[0]
	# else:
	# 	return False

	# v2.5
	# return sorted(dct.items(), key=lambda kv: kv[1], reverse=True)[2][0] if len(dct) > 2 else False


	# v1
	if len(dct) > 2:
		rank_three = sorted([value for key, value in dct.items()], reverse=True)[2]
		return "".join([key for key, value in dct.items() if value == rank_three])
	else:
		return False

print(third_most_expensive({}))
print(third_most_expensive({"piano": 100}))
print(third_most_expensive({"piano": 100, "stereo": 200 }))
print(third_most_expensive({"piano": 100, "stereo": 200, "tv": 10, "timmy": 500 }))
print(third_most_expensive({"piano": 100, "stereo": 200, "tv": 10 }))
print(third_most_expensive({"computer": 1000, "piano": 500, "stereo": 200, "tv": 10, "timmy": 1 }))