"""
Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).

Examples
vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False
"""
def vowel_links(txt):

    txt = list(txt)
    vowels = ["a", "i", "u", "e", "o"]

    for i, j in enumerate(txt):
        if j == " ":
            if txt[i-1] in vowels and txt[i+1] in vowels:
                return True
                break
    return False

print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
print(vowel_links("a sudden applause"))
print(vowel_links("the sudden applause"))