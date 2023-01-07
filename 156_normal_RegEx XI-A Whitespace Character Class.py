"""
RegEx XI-A: Whitespace Character Class
Write the regular expression that will match all open compound words (separated by a space) starting with the word best and with a second word that begins with a b. Use the character class \s in your expression.

Example
txt = "best buy best car best friend best-boy bestguest best dressed best bet best man best deal best boyfriend"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["best buy", "best bet", "best boyfriend"]
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
Find more info on RegEx and character classes in Resources.
You can find all the challenges of this series in my Basic RegEx collection.
"""

import re

pattern = 'best\sb\w+'

txt = "best buy best car best friend best-boy bestguest best dressed best bet best man best deal best boyfriend"

print(re.findall(pattern, txt))






