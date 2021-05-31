"""
Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.

Examples
does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True

does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
# Capitalization and punctuation should not matter.

does_rhyme("You are off to the races", "a splendid day.") ➞ False

does_rhyme("and frequently do?", "you gotta move.") ➞ False
Notes
Case insensitive.
Here we are disregarding cases like "thyme" and "lime".
We are also disregarding cases like "away" and "today" (which technically rhyme, even though they contain different vowels).
"""
import re

def does_rhyme(txt1, txt2):

    li = ['a', 'e', 'i', 'o', 'u']

    txt1 = re.sub(r"[^a-zA-Z0-9]"," ", txt1).split()[-1].lower()
    txt2 = re.sub(r"[^a-zA-Z0-9]"," ", txt2).split()[-1].lower()

    for i in txt1:
        if i in li:
            txt1 = txt1[txt1.index(i):]

    for j in txt2:
        if j in li:
            txt2 = txt2[txt2.index(j):]

    return txt1 == txt2

print(does_rhyme("Sam I am!", "Green eggs and ham."))
print(does_rhyme("Sam I am!", "Green eggs and HAM."))
print(does_rhyme("You are off to the races", "a splendid day."))
print(does_rhyme("and frequently do?", "you gotta move."))

