"""
October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase,
so write a function to normalize a sentence.

Create a function that takes a string.
If the string is all uppercase characters,
convert it to lowercase and add an exclamation mark at the end.

Examples
normalize("CAPS LOCK DAY IS OVER") ➞ "Caps lock day is over!"
normalize("Today is not caps lock day.") ➞ "Today is not caps lock day."
normalize("Let us stay calm, no need to panic.") ➞ "Let us stay calm, no need to panic."
Notes
Each string is a sentence and should start with an uppercase character.
"""

def normalize(txt):

    if txt.isupper():
        txt = txt.lower()
        return ''.join([i[1].upper() if i[0] == 0 else i[1] for i in enumerate(txt)]) + '!'
    else:
        return txt

print(normalize("CAPS LOCK DAY IS OVER"))
print(normalize("Today is not caps lock day."))
print(normalize("WE WANT THIS COVID THING TO BE OVER"))
print(normalize("Let us stay calm, no need to panic."))
print(normalize("DO NOT SHOUT"))
print(normalize("Civilized conversation."))
