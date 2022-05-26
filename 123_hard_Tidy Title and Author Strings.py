"""
Tidy Title and Author Strings
You have a list of strings, each consisting of a book title and an author's name.

To illustrate:

[
  ["   Death of a Salesman - Arthur Miller    "],
  ["   Macbeth - William Shakespeare    "],
  ["    A Separate Peace - John Knowles     "],
  [" Lord of the Flies - William Golding"],
  ["A Tale of Two Cities - Charles Dickens"]
]
Create a function that takes a list like the one above and transforms it into the same format as the one below:

[
  ["Death of a Salesman", "Arthur Miller"],
  ["Macbeth", "William Shakespeare"],
  ["A Separate Peace", "John Knowles"],
  ["Lord of the Flies", "William Golding"],
  ["A Tale of Two Cities", "Charles Dickens"]
]
Examples
tidy_books([
  ["     The Catcher in the Rye - J. D. Salinger    "],
  ["    Brave New World - Aldous Huxley   "],
  ["    Of Mice and Men - John Steinbeck    "]
]) ➞ [
  ["The Catcher in the Rye", "J. D. Salinger"],
  ["Brave New World", "Aldous Huley"],
  ["Of Mice and Men", "John Steinbeck"]
]
Notes
Some of these entries have excess white space. Remove this white space in your final output.
"""

def tidy_books(lst):

	all_total = []
	sub_total = []
	temp = []

	for words in lst:
		for word in words:
			count_word = len(word)
			for txt in word:
				temp.append("".join(txt))
				count_word -= 1
				if txt == "-":
					temp.pop()
					sub_total.append("".join(temp).strip())
					temp = []
				if count_word == 0:
					sub_total.append("".join(temp).strip())
					temp = []

		all_total.append(sub_total)
		sub_total = []

	return all_total

print(tidy_books([
  ["   Death of a Salesman - Arthur Miller    "],
  ["   Macbeth - William Shakespeare    "],
  ["    A Separate Peace - John Knowles     "],
  [" Lord of the Flies - William Golding"],
  ["A Tale of Two Cities - Charles Dickens"]
]))

print(tidy_books([
  ["     The Catcher in the Rye - J. D. Salinger    "],
  ["    Brave New World - Aldous Huxley   "],
  ["    Of Mice and Men - John Steinbeck    "]
]))