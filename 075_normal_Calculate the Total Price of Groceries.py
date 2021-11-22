"""
Calculate the Total Price of Groceries
Create a function that takes a list of dictionaries (groceries) which calculates the total price and returns it as a number. A grocery dictionary has a product, a quantity and a price, for example:

{
  "product": "Milk",
  "quantity": 1,
  "price": 1.50
}
Examples
# 1 bottle of milk:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 }
]) ➞ 1.5

# 1 bottle of milk & 1 box of cereals:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }
]) ➞ 4

# 3 bottles of milk:
get_total_price([
  { "product": "Milk", "quantity": 3, "price": 1.50 }
]) ➞ 4.5

# Several groceries:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Eggs", "quantity": 12, "price": 0.10 },
  { "product": "Bread", "quantity": 2, "price": 1.60 },
  { "product": "Cheese", "quantity": 1, "price": 4.50 }
]) ➞ 10.4

# Some cheap candy:
get_total_price([
  { "product": "Chocolate", "quantity": 1, "price": 0.10 },
  { "product": "Lollipop", "quantity": 1, "price": 0.20 }
]) ➞ 0.3
Notes
There might be a floating point precision problem in here...
"""

def get_total_price(groceries):

	return round(sum([key["quantity"] * key["price"] for key in groceries]), 2)


print(get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }
]))

print(get_total_price([
	{ "product": "Milk", "quantity": 3, "price": 1.50 }
]))

print(get_total_price([
	{ "product": "Chocolate", "quantity": 1, "price": 0.10 },
	{ "product": "Lollipop", "quantity": 1, "price": 0.20 }
]))