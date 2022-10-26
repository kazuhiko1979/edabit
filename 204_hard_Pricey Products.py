"""
Pricey Products
You will be given a dictionary with various products and their respective prices. Return a list of the products with a minimum price of 500 in descending order.

Examples
pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50}) ➞ ["TV", "Computer"]

pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}) ➞ ["Bike1", "Bike3"]

pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20}) ➞ []
"""

# v2
def pricey_prod(d):

	return sorted((k for k, v in d.items() if v >= 500), key=lambda x: -d[x])

# v1
# def pricey_prod(dict):
#
# 	lst = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]))
# 	lst.sort(key=lambda x: x[1], reverse=True)
# 	return [k for k, v in lst if v >= 500]


print(pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50}))
print(pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}))
print(pricey_prod({'Calvin Klein' : 500, 'Armani' : 5000, 'Dolce & Gabbana' : 2000}))
print(pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20}))
print(pricey_prod({'Dell' : 400, 'HP' : 300, 'Apple' : 1200}))

