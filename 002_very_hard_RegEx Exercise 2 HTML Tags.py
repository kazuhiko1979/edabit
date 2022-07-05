"""
RegEx Exercise #2: HTML Tags
Write three regular expressions:

One called opening_tags that will match all HTML opening tags including attributes.
One called closing_tags that will match all HTML closing tags.
One called all_tags that will match all HTML tags opening or closing, their attributes and their content (as long as their content is in the same line). Please, check the example below to see the expected result.
Example
index = '''
<html>
<head>
    Hi! I'm a text in the head.
    I probably shouldn't be here.
    <title>edabit.com</title>
</head>
<body>
    Hi! I'm a text in the body.
    <p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>
    Here comes a fake tag: <>.
</body>
</html>
'''

opening_tags = "yourregularexpressionhere"
closing_tags = "yourregularexpressionhere"
all_tags = "yourregularexpressionhere"

re.findall(opening_tags, index) ➞ ["<html>", "<head>", "<title>", "<body>", "<p>", "<a href="https://edabit.com">"]

re.findall(closing_tags, index) ➞ ["</title>", "</head>",  "</a>", "</p>", "</body>", "</html>"]

re.findall(all_tags, index) ➞ ["<html>", "<head>", "<title>edabit.com</title>", "</head>", "<body>", "<p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>", "</body>", "</html>"]
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the cod
"""

import re

index = '''
<html>
<head>
    Hi! I'm a text in the head.
    I probably shouldn't be here.
    <title>edabit.com</title>
</head>
<body>
    Hi! I'm a text in the body.
    <p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>
    Here comes a fake tag: <>.
</body>
</html>
'''

# opening_tag = '<[^/].*?>'
# closing_tag = '</.+?>'
# all_tag = '<.+>'

# opening_tag = '<\w+.*?>'
# closing_tag = '</\w+>'
# all_tag = '</?\w+.*>'


opening_tag = '<[a-z].*?>'
closing_tag = '</.*?>'
all_tag = '<.+>'


print(re.findall(opening_tag, index))
print(re.findall(closing_tag, index))
print(re.findall(all_tag, index))