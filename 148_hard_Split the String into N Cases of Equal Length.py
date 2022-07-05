"""
Split the String into N Cases of Equal Length
Create a function that accepts txt and cases as parameters where the string is split into N distinct cases of equal length as shown:

Examples
split_n_cases("Strengthened", 6) ➞ ["St", "re", "ng", "th", "en", "ed"]

split_n_cases("Unscrupulous", 2) ➞ ["Unscru", "pulous" ]

split_n_cases("Flavorless", 1) ➞ ["Flavorless" ]
Notes
If it's not possible to split the string as described, return ["Error"].
"""

def split_n_cases(txt, cases):

	# v1
	length_of_txt = divmod(len(txt), cases)
	return [txt[i:i+length_of_txt[0]] for i in range(0, len(txt), length_of_txt[0])] if length_of_txt[1] == 0 else ["Error"]

print(split_n_cases("Strengthened", 6))
print(split_n_cases("Unscrupulous", 2))
print(split_n_cases("Flavorless", 1))
print(split_n_cases("Fool's Errand", 20))
print(split_n_cases("Evolutionary Biology", 8))

