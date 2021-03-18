"""
In music, cadences act as punctuation in musical phrases, and help to mark the end of phrases. Cadences are the two chords at the end of a phrase. The different cadences are as follows:

V followed by I is a Perfect Cadence
IV followed by I is a Plagal Cadence
V followed by Any chord other than I is an Interrupted Cadence
Any chord followed by V is an Imperfect Cadence
Create a function where given a chord progression as a list, return the type of cadence the phrase ends on.

Examples
find_cadence(["I", "IV", "V"]) ➞ "imperfect"
find_cadence(["ii", "V", "I"]) ➞ "perfect"
find_cadence(["I", "IV", "I", "V", "vi"]) ➞ "interrupted"

Notes
Return strings all in lowercase.
Only focus on the last two chords of a progression.
Return "no cadence" if none of the criterea match up.
I is a capital i not a lowercase L.
"""
def find_cadence(chords):

    last_two_chords = chords[-2]
    last_chords = chords[-1]

    if last_chords == "V":
        return "imperfect"

    if last_two_chords == "V" and last_chords == "I":
        return "perfect"
    elif last_two_chords == "IV" and last_chords == "I":
        return "plagal"
    elif last_two_chords == "V" and last_chords != "I":
        return "interrupted"
    else:
        return "no cadence"


print(find_cadence(["I", "IV", "V"]))
print(find_cadence(["ii", "V", "I"]))
print(find_cadence(["I", "IV", "I", "V", "vi"]))
print(find_cadence(["I", "IV", "I", "V", "IV"]))
print(find_cadence(["I", "III", "IV", "V"]))
print(find_cadence(["I", "IV", "I"]))
print(find_cadence(["V", "IV", "I"]))
print(find_cadence(["V", "IV", "V", "I"]))
print(find_cadence(["V", "IV", "V", "I", "vi"]))
print(find_cadence(["V", "IV", "V", "III", "vi"]))

