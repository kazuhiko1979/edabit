"""
RegEx VIII-A: Digit Character Class
Write the regular expression that matches all street addresses. All street addresses begin with a number. Use the character class \d in your expression.

Example
txt = "123 Redding Dr. 1560 Knoxville Ave. 3030 Norwalk Dr. 5 South St."
pattern = "yourregularexpressionhere"

(re.findall(pattern, txt)) ➞ ["123 Redding Dr.", "1560 Knoxville Ave.", "3030 Norwalk Dr.", "5 South St."]
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
Find more info on RegEx and character classes in Resources.
You can find all the challenges of this series in my Basic RegEx collection.
"""

import re

txt = "123 Redding Dr. 1560 Knoxville Ave. 3030 Norwalk Dr. 5 South St."

# pattern = r'[^.]+(?:[.]|$)'
pattern = '\d+\D*\.'
pattern = '\d+[^.]+.'
pattern = r'\d+ \w+ \w+.'

txt = re.findall(pattern, txt)
print(txt)

# res = []
#
# for i in txt:
#     if [i][0] != '':
#         new_i = i.strip()
#         res.append(new_i)
#     else:
#         res.append(i)
# print(res)

