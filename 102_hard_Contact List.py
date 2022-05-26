"""
Contact List
Write a sorting function that takes in a list of names and sorts them by last name either alphabetically (ASC) or reverse-alphabetically (DESC).

Examples
sort_contacts([
  "John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"
], "ASC") ➞ [
  "Thomas Aquinas",
  "Rene Descartes",
  "David Hume",
  "John Locke"
]

# Aquinas (A) < Descartes (D) < Hume (H) < Locke (L)

sort_contacts([
  "Paul Erdos",
  "Leonhard Euler",
  "Carl Gauss"
], "DESC") ➞ [
  "Carl Gauss",
  "Leonhard Euler",
  "Paul Erdos"
]

# Gauss (G) > Erdos (ER) > Euler (EU)

sort_contacts([], "DESC") ➞ []

sort_contacts(None, "DESC") ➞ []
Notes
A list with a single name should be trivially returned.
An empty list, or an input of None should return an empty list.
"""

# v3
def sort_contacts(names, sort):

	return sorted(names or [], key=lambda x:x.split()[1], reverse=sort!='ASC')


# v2
# def sort_contacts(names, sort):
#
# 	if not names:
# 		return []
# 	names.sort(key=lambda x : x.split()[1])
# 	return names if sort == "ASC" else names[::-1]


# v1
# def sort_contacts(names, sort):
#
# 	if names != None:
# 		if sort == "DESC":
# 			names = sorted(names, key=lambda x: x.split()[1], reverse=True)
# 			return names
# 		elif sort == "ASC":
# 			names = sorted(names, key=lambda x: x.split()[1], reverse=False)
# 			return names
# 	return []


print(sort_contacts([
  "John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"
], "ASC"))

print(sort_contacts([
	'Paul Erdos',
	'Leonhard Euler',
	'Carl Gauss'
], 'DESC'))


print(sort_contacts([
	'Michael Phelps',
	'Jesse Owens',
	'Michael Jordan',
	'Usain Bolt'
], 'DESC'))

print(sort_contacts(['Al Gore',
					 'Barack Obama'
					 ], 'ASC'))

print(sort_contacts(['Albert Einstein'], 'ASC'))

print(sort_contacts([], 'DESC'))

print(sort_contacts(None, 'DESC'))

