"""
Fruit Smoothie
Create a class Smoothie and do the following:

Create an instance attribute called ingredients.
Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
Ingredient	Price
Strawberries	$1.50
Banana	$0.50
Mango	$2.50
Blueberries	$1.00
Raspberries	$1.00
Apple	$1.75
Pineapple	$3.50
Examples
s1 = Smoothie(["Banana"])

s1.ingredients ➞ ["Banana"]

s1.get_cost() ➞ "$0.50"

s1.get_price() ➞ "$1.25"

s1.get_name() ➞ "Banana Smoothie"
s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])

s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]

s2.get_cost() ➞ "$3.50"

s2.get_price() ➞ "$8.75"

s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"
"""

# My Code:


prices = {
	"Strawberries" : "$1.50",
	"Banana" : "$0.50",
	"Mango" : "$2.50",
	"Blueberries" : "$1.00",
	"Raspberries" : "$1.00",
	"Apple" : "$1.75",
	"Pineapple" : "$3.50"
}

# v2
class Smoothie:

	def __init__(self, ingredients):
		self.ingredients = ingredients
		self.cost = sum(float(prices[i][1:]) for i in self.ingredients)

	def get_cost(self):
		return "${:0.2f}".format(self.cost)

	def get_price(self):
		return "${:0.2f}".format(self.cost * 2.5)

	def get_name(self):
		name = ' '.join(sorted(i.replace('rries', 'rry') for i in self.ingredients))
		return name + " " + ('smoothie', 'Fusion')[len(self.ingredients) > 1]


# v1
# class Smoothie:
#
# 	def __init__(self, ingredients):
# 		self.ingredients = ingredients
#
# 	def get_price(self):
# 		cost = sum(float(prices[i][1:]) for i in self.ingredients)
# 		return '$' + '{:.2f}'.format(cost + (cost * 1.5))
#
# 	def get_cost(self):
# 		cost = sum(float(prices[i][1:]) for i in self.ingredients)
# 		return '$' + '{:.2f}'.format(cost)
#
# 	def get_name(self):
# 		temp = [ingredient.replace('ies', 'y') if 'ies' in ingredient[-3:] else ingredient for ingredient in self.ingredients]
# 		if len(temp) == 1:
# 			return ' '.join(sorted(temp)) + ' Smoothie'
# 		else:
# 			return ' '.join(sorted(temp)) + ' Fusion'

s1 = Smoothie(["Banana"])
s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
s3 = Smoothie(["Mango", "Apple", "Pineapple"])
s4 = Smoothie(["Pineapple", "Strawberries", "Blueberries", "Mango"])
s5 = Smoothie(["Blueberries"])

print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())

print(s2.ingredients)
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())

print(s3.ingredients)
print(s3.get_cost())
print(s3.get_price())
print(s3.get_name())

print(s4.ingredients)
print(s4.get_cost())
print(s4.get_price())
print(s4.get_name())


print(s5.ingredients)
print(s5.get_cost())
print(s5.get_price())
print(s5.get_name())


