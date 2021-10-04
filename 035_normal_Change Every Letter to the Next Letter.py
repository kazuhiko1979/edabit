"""
Write a function that changes every letter to the next letter:

"a" becomes "b"
"b" becomes "c"
"d" becomes "e"
and so on ...
Examples
move("hello") ➞ "ifmmp"

move("bye") ➞ "czf"

move("welcome") ➞ "xfmdpnf"
Notes
There will be no z's in the tests.
"""
# import string

def move(word):

    return ''.join(chr(ord(i)+1) for i in word)

    # letters = string.ascii_lowercase
    # return ''.join([''.join(letters[letters.index(i) + 1]) for i in word if i in letters])


print(move("hello"))
print(move("lol"))
print(move("bye"))

