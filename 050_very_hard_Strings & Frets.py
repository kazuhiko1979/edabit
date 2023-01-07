"""
Strings & Frets
Write a function that gets a string number and a fret of a 6-string guitar in 'standard tuning' and return the corresponding note. For this challenge we use a 24 fret model.

The notes are:

C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B
Try not to use a 2 dimensional list. Look at the image on the bottom to see the note names on the guitar neck.

Examples
string_fret(2, 10) ➞ "A"

string_fret(0, 16) ➞ "Invalid input"

string_fret(2, 19) ➞ "F#/Gb"

string_fret(3, 0) ➞ "G"
Notes
If the string or fret number isn't correct return "Invalid input".
"""

code = "C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B".split()
C_START = (None, 4, 11, 7, 2, 9, 4)

def string_fret(st, fr):
	if 0 < st < 7 and 0 <= fr <= 24:
		return code[(C_START[st]+fr) % 12]
	return "Invalid input"


# v1
# code = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
#
# def string_fret(st, fr):
#
# 	if not 1 <= st <= 6 or fr > 24:
# 		return "Invalid input"
#
# 	guiter_neck = {
# 		1: 8,
# 		2: 1,
# 		3: 5,
# 		4: 10,
# 		5: 3,
# 		6: 8
# 	}
# 	index = guiter_neck[st]
# 	return code[fr - 12 - index] if fr - index > 12 else code[fr - index]

print(string_fret(2, 10))
print(string_fret(6, 3))
print(string_fret(1, 18))
print(string_fret(0, 16))
print(string_fret(3, 1))
print(string_fret(5, 3))
print(string_fret(5, 25))
print(string_fret(6, 13))
print(string_fret(4, 18))


print(string_fret(2, 19))

print(string_fret(4, 5))
print(string_fret(6, 10))
print(string_fret(2, 10))
print(string_fret(3, 0))






