"""
Tidy Hyperlinks
Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier like this. Notice how the text "Go to the challenges!" appears when hovering over the link.

This was achieved by using this code:

[this](https://edabit.com/challenges "Go to the challenges!")
Given the url, the new name and optionally the hover_text, return the tidied up hyperlink as a string.

Examples
tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!") ➞ "[this](https://edabit.com/challenges "Go to the challenges!")"

tidy_link("https://www.google.com", "Google", "Google Search") ➞ "[Google](https://www.google.com "Google Search")"

tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!") ➞ "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
Notes
Supply double quotes for the hover text.
Keep in mind that some tests will not include an argument for hover_text.
Test.assert_equals(tidy_link('https://edabit.com/challenges', 'Challenges', 'Go to the challenges!'), '[Challenges](https://edabit.com/challenges "Go to the challenges!")')
Test.assert_equals(tidy_link('https://www.google.com', 'Google', 'Google Search'), '[Google](https://www.google.com "Google Search")')
Test.assert_equals(tidy_link('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Click Me!'), '[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)')
Test.assert_equals(tidy_link('https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet', 'Markdown Cheatsheet'), '[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)')
Test.assert_equals(tidy_link('https://www.python.org/', 'Python', 'Visit the Python Website!'), '[Python](https://www.python.org/ "Visit the Python Website!")')
Test.assert_equals(tidy_link('https://www.youtube.com/watch?v=O2yPnnDfqpw', 'i just did a bad thing'), '[i just did a bad thing](https://www.youtube.com/watch?v=O2yPnnDfqpw)')
Test.assert_equals(tidy_link('https://www.reddit.com/', 'Reddit', 'the front page of
"""

# v1
# def tidy_link(url, name, hover_text=""):
#
# 	if not hover_text:
# 		return '[{}]{}'.format(str(name), '(' + url + ')')
# 	return '[{}]{} {}'.format(str(name), '(' + url, '"' + hover_text + '"' + ')')

print(tidy_link('https://edabit.com/challenges', 'Challenges', 'Go to the challenges!'))
print(tidy_link('https://www.google.com', 'Google', 'Google Search'))
print(tidy_link('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Click Me!'))
print(tidy_link('https://www.python.org/', 'Python', 'Visit the Python Website!'))




# '[Challenges](https://edabit.com/challenges "Go to the challenges!")
# '[Challenges](https://edabit.com/challenges "Go to the challenges!")'
