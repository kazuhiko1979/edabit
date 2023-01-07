"""
RegEx V: Negative Lookahead
Write a regular expression that will match the states that voted no to President Trump's impeachment. You must use RegEx negative lookahead. You are not allowed to use positive lookaheads.

Example
txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["Texas", "Michigan"]
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
This is fake data and used only for educational purposes.
"""

import re

pattern = '(\w+) (?!= yes)'


for i in txt.split(','):
	print(re.search(pattern, i))
	# print(result)
# print(result)


# print([i.rsplit()[0] for i in txt.split(',') if i.rsplit()[-1] == 'no'])


# example = re.search(r'(?<=geeks)\w',
# 					'geeksforgeeks')
#
# print(example.group())
# print("Pattern found from index",
# 	  example.start(), example.end())