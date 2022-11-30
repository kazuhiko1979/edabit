"""
Awarding Prizes
You are given a dictionary of names and the amount of points they have. Return a dictionary with the same names, but instead of points, return what prize they get.

"Gold", "Silver", or "Bronze" to the 1st, 2nd and 3rd place respectively. For all the other names, return "Participation" for the prize.

Examples
award_prizes({
  "Joshua" : 45,
  "Alex" : 39,
  "Eric" : 43
}) ➞ {
  "Joshua" : "Gold",
  "Alex" : "Bronze",
  "Eric" : "Silver"
}

award_prizes({
  "Person A" : 1,
  "Person B" : 2,
  "Person C" : 3,
  "Person D" : 4,
  "Person E" : 102
}) ➞ {
  "Person A" : "Participation",
  "Person B" : "Participation",
  "Person C" : "Bronze",
  "Person D" : "Silver",
  "Person E" : "Gold"
}

award_prizes({
  "Mario" : 99,
  "Luigi" : 100,
  "Yoshi" : 299,
  "Toad" : 2
}) ➞ {
  "Mario" : "Bronze",
  "Luigi" : "Silver",
  "Yoshi" : "Gold",
  "Toad" : "Participation"
}
Notes
There will always be at least three participants to recieve awards.
No number of points will be the same amongst participants.
"""

def award_prizes(names):

	awards = ["Gold", "Silver", "Bronze"] + ["Participation"] * (len(names) - 3)
	ranked = sorted(names, key=names.get, reverse=True)
	return dict(zip(ranked, awards))




# def award_prizes(dic):
#
# 	values = list(dic.values())
#
# 	Gold = sorted(values, reverse=True)[0]
# 	Silver = sorted(values, reverse=True)[1]
# 	Bronze = sorted(values, reverse=True)[2]
#
# 	for key, value in dic.items():
# 		if value == Gold:
# 			dic[key] = "Gold"
# 			continue
# 		if value == Silver:
# 			dic[key] = "Silver"
# 			continue
# 		if value == Bronze:
# 			dic[key] = "Bronze"
# 			continue
# 		else:
# 			dic[key] = "Participation"
#
# 	return dic


print(award_prizes({
  "Joshua" : 45,
  "Alex" : 39,
  "Eric" : 43
}))

print(award_prizes({
  "Person A" : 1,
  "Person B" : 2,
  "Person C" : 3,
  "Person D" : 4,
  "Person E" : 102
}))

print(award_prizes({
  "Mario" : 99,
  "Luigi" : 100,
  "Yoshi" : 299,
  "Toad" : 2
}))