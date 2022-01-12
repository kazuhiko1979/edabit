"""
Extending The String
Make two functions:

consonants(word) which returns the number of consonants in a word when called.
vowels(word) which returns the number of vowels in a word when called.
Examples
vowels('Jameel SAEB') ➞ 5

consonants('He|\o mY Fr*end') ➞ 7

consonants("Smithsonian") ➞ 7
vowels("Smithsonian") ➞ 4
Notes
Vowels are: a, e, i, o, u.
Spaces and special character do not count as consonants nor vowels.
"""

def vowels(txt):

    count = 0
    txt = txt.lower()
    for i in txt:
        if i in 'aiueo':
            count += 1
    return count

def consonants(txt):

    count = 0
    txt = txt.lower()
    for i in txt:
        if i.isalpha():
            if i not in 'aiueo':
                count += 1
    return count


print(vowels('Jameel SAEB'))
print(consonants('He|\o mY Fr*end'))
print(vowels("Smithsonian"))