"""
Create a function that returns the whole of the first sentence which contains a specific word. Include the full stop at the end of the sentence.

Examples
txt = "I have a cat. I have a mat. Things are going swell."

sentence_searcher(txt, "have") ➞ "I have a cat."

sentence_searcher(txt, "MAT") ➞ "I have a mat."

sentence_searcher(txt, "things") ➞ "Things are going swell."

sentence_searcher(txt, "flat") ➞ ""
Notes
Sentences will always end with full stops.
Your function should not be case sensitive.
Return an empty string if the word isn't found in the sentence.
"""

txt = "I have a cat. I have a mat. Things are going swell."


def sentence_searcher(txt, word):

    txt = [s + '.' for s in txt.split('.')]
    txt.pop(-1)

    for i in txt:
        if word.lower() in i.lower():
            return i.lstrip()
            break
    return ""

print(sentence_searcher(txt, "have"))
print(sentence_searcher(txt, "MAT"))
print(sentence_searcher(txt, "things"))
print(sentence_searcher(txt, "flat"))

