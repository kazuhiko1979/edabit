"""
Given two sentences, return whether they are shadows of each other. This means that all of the word lengths are the same, but the corresponding words don't share any common letters.

Examples
shadow_sentence("they are round", "fold two times") ➞ True

shadow_sentence("own a boat", "buy my wine") ➞ False
# No words share common letters, but "a" and "my" have different lengths.

shadow_sentence("his friends", "our company") ➞ False
# Word lengths are the same but "friends" and "company" share the letter "n".

shadow_sentence("salmonella supper", "birthright") ➞ False
# Setences with different numbers of words.
Notes
All sentences will be given in lowercase, and will have no punctuation.
Return False if the sentences have different numbers of words.
"""

def shadow_sentence(s1, s2):

    total_s1 = 0
    s1_s = s1.split(" ")
    for i in s1_s:
        total_s1 += int(s1_s.count(i))

    total_s2 = 0
    s2_s = s2.split(" ")
    for i in s2_s:
        total_s2 += int(s2_s.count(i))

    if total_s1 != total_s2:
        return False

    for a, b in zip(s1.split(), s2.split()):
        if len(a) != len(b):
            return False

        length = [i for i in range(len(b))]
        p = [p for p in range(1, len(b)+1)]

    for i, p0 in zip(length, p):
        substr = b[i:p0]
        if substr in a:
            return False
        # break
    return True

print(shadow_sentence("they are round", "fold two times"))
print(shadow_sentence("own a boat", "buy my wine"))
print(shadow_sentence("his friends", "our company"))
print(shadow_sentence('impossible poetry', 'gargantuan cliffs'))
print(shadow_sentence('a normal sentence', 'a normal sentence'))
print(shadow_sentence("own a boat", "buy my wine"))
print(shadow_sentence('salmonella supper', 'birthright'))