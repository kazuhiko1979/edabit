"""
RegEx IV: Positive Lookahead
Write a regular expression that will match the states that voted yes to President Trump's impeachment. You must use RegEx positive lookahead.

Example
txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["California", "Florida"]
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
This is fake data and used only for educational purposes.
"""

import re

txt = "Texas = no, California = yes, Florida = yes, Michigan = no"


# pattern = "(\w+) = yes"


# use positive Lookahead
pattern = "\w+(?= = yes)"

print(re.findall(pattern, txt))


