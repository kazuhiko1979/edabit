"""
Vending Machine
Your task is to create a function that simulates a vending machine.

Given an amount of money (in cents ¢ to make it simpler) and a product_number, the vending machine should output the correct product name and give back the correct amount of change.

The coins used for the change are the following: [500, 200, 100, 50, 20, 10]

The return value is a dictionary with 2 properties:

product: the product name that the user selected.
change: an array of coins (can be empty, must be sorted in descending order).
Examples
vending_machine(products, 200, 7) ➞ { "product": "Crackers", "change": [ 50, 20, 10 ] }

vending_machine(products, 500, 0) ➞ "Enter a valid product number"

vending_machine(products, 90, 1) ➞ "Not enough money for this product"
Notes
The products are fixed and you can find them in the Tests tab.
If product_number is invalid (out of range) you should return the string: "Enter a valid product number".
If money is not enough to buy a certain product you should return the string: "Not enough money for this product".
If there's no change, return an empty array as the change.
"""
products = [
  { 'number': 1, 'price': 100, 'name': 'Orange juice' },
  { 'number': 2, 'price': 200, 'name': 'Soda' },
  { 'number': 3, 'price': 150, 'name': 'Chocolate snack' },
  { 'number': 4, 'price': 250, 'name': 'Cookies' },
  { 'number': 5, 'price': 180, 'name': 'Gummy bears' },
  { 'number': 6, 'price': 500, 'name': 'Condoms' },
  { 'number': 7, 'price': 120, 'name': 'Crackers' },
  { 'number': 8, 'price': 220, 'name': 'Potato chips' },
  { 'number': 9, 'price': 80,  'name': 'Small snack' }
]
changes = [500, 200, 100, 50, 20, 10]

# v3
def vending_machine(products, money, num):
	if num not in range(1, 10):
		return "Enter a valid product number"
	if money < products[num-1]['price']:
		return "Not enough money this product"

	money -= products[num-1]['price']
	change = []

	for i in changes:
		change.extend([i] * (money//i))
		money %= i
	return {'product': products[num-1]['name'], 'change': change}

# v2
# def vending_machine(products, money, product_number):
#
# 	if product_number not in range(1, len(products)+1):
# 		return "Enter a valid product number"
#
# 	product = products[product_number - 1]
# 	owed = money - product['price']
# 	if owed < 0:
# 		return "Not enough money for this product"
# 	coins = []
# 	i = 0
# 	while owed > 0:
# 		while owed < changes[i]:
# 			i += 1
# 		coins.append(changes[i])
# 		owed -= changes[i]
# 	return {'change': coins, 'product':product['name']}







# v1
# products = [
#   { 'number': 1, 'price': 100, 'name': 'Orange juice' },
#   { 'number': 2, 'price': 200, 'name': 'Soda' },
#   { 'number': 3, 'price': 150, 'name': 'Chocolate snack' },
#   { 'number': 4, 'price': 250, 'name': 'Cookies' },
#   { 'number': 5, 'price': 180, 'name': 'Gummy bears' },
#   { 'number': 6, 'price': 500, 'name': 'Condoms' },
#   { 'number': 7, 'price': 120, 'name': 'Crackers' },
#   { 'number': 8, 'price': 220, 'name': 'Potato chips' },
#   { 'number': 9, 'price': 80,  'name': 'Small snack' }
# ]
# changes = [500, 200, 100, 50, 20, 10]
#
#
# def vending_machine(products, money, product_number) -> dict:
#
# 	if product_number <= 0:
# 		return 'Enter a valid product number'
#
# 	for product in products:
# 		for key, value in product.items():
# 			if key == 'number' and value == product_number:
# 				return calc_change(product['name'], money - product['price'])
#
# def calc_change(product, money, index=0, change=[]):
#
# 	if money == 0:
# 		ori_change = change.copy()
# 		change.clear()
# 		return { "product": product, "change": ori_change }
# 	elif money < 0:
# 		return 'Not enough money for this product'
#
# 	if money >= changes[index]:
# 		if money in change:
# 			change.append(changes[index])
# 			money -= changes[index]
# 			return calc_change(product, money, index+1, change)
# 		else:
# 			change.append(changes[index])
# 			money -= changes[index]
# 			return calc_change(product, money, index, change)
# 	else:
# 		return calc_change(product, money, index+1, change)


print(vending_machine(products, 500, 8))
print(vending_machine(products, 200, 7))
print(vending_machine(products, 500, 1))
print(vending_machine(products, 100, 9))
print(vending_machine(products, 1000, 6))
print(vending_machine(products, 250, 4))
print(vending_machine(products, 500, 0))
print(vending_machine(products, 90, 1))
print(vending_machine(products, 0, 0))