"""
RegEx Exercise #4: Edit the Body Element
Write three regular expressions that will be passed to re.sub() in order to modify the body element in our HTML file:

One called body_insert that will be used to add elements immediately after the body element opening tag: <body>.
One called body_append that will be used to add elements immediately before the body element closing tag: </body>.
One called body_rewrite that will be used to replace the content of the body element: <body>content</body>.
Details to take into account:

The opening tag <body> will be followed by line break \n, you should match after the line break.
The closing tag </body> will be preceded by line break \n, you should match before the line break.
You do not need to worry about the inserted elements' formatting, it's already been taken care of.
body_rewrite should match the content of the body element, but not the body tags.
The content of the body element may be in more than one line.
Example
index = '''
<body>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
</body>
'''

body_insert = "yourregularexpressionhere"
body_append = "yourregularexpressionhere"
body_rewrite = "yourregularexpressionhere"
body_insert
re.sub(body_insert, '    <p>Pre-Paragraph</p>\n', index) ➞
'''
<body>
    <p>Pre-Paragraph</p>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
</body>
'''
body_append
re.sub(body_append, '\n    <p>Post-Paragraph</p>', index) ➞
'''
<body>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
    <p>Post-Paragraph</p>
</body>
'''
body_rewrite
re.sub(body_rewrite, '    <p>Anti-Paragraph</p>', index) ➞
'''
<body>
    <p>Anti-Paragraph</p>'
</body>
'''
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
"""
import re

body_insert = '(?<=<body>\n)'
body_append = '(?=\n</body>)'
body_rewrite = '{}[\s\S]+{}'.format(body_insert, body_append)




