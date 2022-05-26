"""
The Frugal Gentleman
Atticus has been invited to a dinner party, and he decides to purchase a bottle of wine. However, he has little knowledge of how to choose a good bottle. Being a very frugal gentleman (yet disliking looking like a cheapskate), he decides to use a very simple rule. In any selection of two or more wines, he will always buy the second-cheapest.

Given a list of wine dictionaries, write a function that returns the name of the wine he will buy for the party. If given an empty list, return None. If given a list of only one, Atticus will buy that wine.

Examples
chosen_wine([
  { "name": "Wine A", "price": 8.99 },
  { "name": "Wine 32", "price": 13.99 },
  { "name": "Wine 9", "price": 10.99 }
]) ➞ "Wine 9"

chosen_wine([{ "name": "Wine A", "price": 8.99 }]) ➞ "Wine A"

chosen_wine([]) ➞ None
Notes
All wines will be different prices, so there is no confusion in the ordering.
"""

def chosen_wine(wines):

	# v2
	if len(wines) == 1:
		return wines[0]["name"]
	return None if not wines else sorted([[i["price"], i["name"]] for i in wines])[1][-1]


	# v1
	# if wines == []:
	# 	return None
	# elif len(wines) == 1:
	# 	return wines[0]['name']
	# else:
	# 	second_price = sorted([wine["price"] for wine in wines])[1]
	# 	for wine in wines:
	# 		if wine["price"] == second_price:
	# 			return wine["name"]


print(chosen_wine([
  { "name": "Wine A", "price": 8.99 },
  { "name": "Wine 32", "price": 13.99 },
  { "name": "Wine 9", "price": 10.99 }
]))

print(chosen_wine([{"name": "Wine A", "price": 8.99},
				   {"name": "Wine B", "price": 9.99}]))
#
print(chosen_wine([{"name": "Wine A", "price": 8.99}]))
#
print(chosen_wine([]))

print((chosen_wine([{"name": "Wine A", "price": 8.99},
					{"name": "Wine 389", "price": 109.99},
					{"name": "Wine 44", "price": 38.44},
					{"name": "Wine 72", "price": 22.77}])))



