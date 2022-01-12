"""
From A to Z
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

Examples
gimme_the_letters("a-z") ➞ "abcdefghijklmnopqrstuvwxyz"

gimme_the_letters("h-o") ➞ "hijklmno"

gimme_the_letters("Q-Z") ➞ "QRSTUVWXYZ"

gimme_the_letters("J-J") ➞ J"
Notes
A hyphen will separate the two letters in the string.
You don't need to worry about error handling in this one (i.e. both letters will be the same case and the second letter will always be after the first alphabetically).
"""

# alphabets = "abcdefghijklmnopqrstuvwxyz"

def gimme_the_letters(spectrum):

    # return "".join([chr(n) for n in range(ord(spectrum[0]), ord(spectrum[-1])+1)])


    # a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # x, y = spectrum.split('-')
    # return a[a.index(x):a.index(y)+1]


    start, end = [ord(i) for i in spectrum.split('-')]
    return ''.join(chr(i) for i in range(start, end+1))



    # start = alphabets.index(spectrum[0].lower())
    # end = alphabets.index(spectrum[-1].lower())
    #
    # if str(spectrum[0] + spectrum[-1]).isupper():
    #     return ''.join([alphabets[i] for i in range(start, end+1)]).upper()
    # return ''.join([alphabets[i] for i in range(start, end + 1)])


print(gimme_the_letters("a-z"))
print(gimme_the_letters("h-o"))
print(gimme_the_letters("Q-Z"))
print(gimme_the_letters("J-J"))


