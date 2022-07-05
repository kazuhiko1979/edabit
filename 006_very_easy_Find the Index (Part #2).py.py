"""
Find the Index (Part #2)
Create a function that searches for the index of a given item in a list. If the item is present, it should return the index, otherwise, it should return -1.

Examples
search([1, 2, 3, 4], 3) ➞ 2

search([2, 4, 6, 8, 10], 8) ➞ 3

search([1, 3, 5, 7, 9], 11) ➞ -1
Notes
If the item is not present, return -1.
The given list is ordered.
"""

def search(lst, item, count=0):

	try:
		if count == lst.index(item):
			return count
		return search(lst, item, count+1)
	except ValueError:
		return -1


print(search([1, 2, 3, 4], 3))
print(search([2, 4, 6, 8, 10], 8))
print(search([1, 3, 5, 7, 9], 11))
print(search([1, 5, 7, 11, 25, 100, 200, 350], 5))