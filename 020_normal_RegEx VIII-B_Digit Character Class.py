"""
Write the regular expression that will match all non-digit characters of a string.
Use the character class \D in your expression.

Example
txt = "242Edabit2345can3443be3254324addictive!"
pattern = "yourregularexpressionhere"

" ".join(re.findall(pattern, txt)) ➞ "Edabit can be addictive!"
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
"""

import re

txt = "242Edabit2345can3443be3254324addictive!"
# [a-z\d]は英数字のうち任意の一文字を意味します。
pattern = "[A-z!?.,]+\D"
# pattern = "[A-z!?\]+\D"

print(" ".join(re.findall(pattern, txt)))

