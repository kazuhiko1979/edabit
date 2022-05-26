"""
RegEx X-B: Word Character Class
Write the regular expression that will help us count how many div elements are there in a string. Use the character class \W in your expression.

Example
txt1 = "<div>Hello.</div><div>My name is <b>George</b>.</div>"
txt2 = "<div><h1>The Word for Today</h1><div>aardvark</div></div>"
txt3 = "<div></div>"
pattern = "yourregularexpressionhere"

len(re.findall(pattern, txt1)) ➞ 2
len(re.findall(pattern, txt2)) ➞ 2
len(re.findall(pattern, txt3)) ➞ 1
Notes
A div element consists of an opening tag, none or some content and a closing tag. For example: <div>Hello.</div>.
Do not count the opening and closing tags as separate elements.
Opening an closing tags will be evenly paired.
HTML elements can be nested.
You don't need to write a function, just the pattern.
Do not remove import re from the code.
"""
import re
txt1 = "<div>Hello.</div><div>My name is <b>George</b>.</div>"
txt2 = "<div><h1>The Word for Today</h1><div>aardvark</div></div>"
txt3 = "<div></div>"

# pattern = "(?<!\w)/div(?!>\w)"

# pattern = "(\W)/div(\W)"
# pattern = r'<div[\W]'
pattern = "\W/div\W"


print(len(re.findall(pattern, txt1)))
print(len(re.findall(pattern, txt2)))
print(len(re.findall(pattern, txt3)))