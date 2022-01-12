"""
Extend the Vowels
Create a function that takes a word and extends all vowels by a number num.

Examples
extend_vowels("Hello", 5) ➞ "Heeeeeelloooooo"

extend_vowels("Edabit", 3) ➞ "EEEEdaaaabiiiit"

extend_vowels("Extend", 0) ➞ "Extend"
Notes
Return "invalid" if num is not an integer.
"""

def extend_vowels(txt, num):

    return 'invalid' if num%1 or num<0 else ''.join(i*(num+1) if i in 'aeiouAEIOU' else i for i in txt)


    # vowels = 'aiueoAIUEO'
    # if num < 0 or type(num) is not int:
    #     return "invalid"
    # return ''.join(c * (num + 1) if c in vowels else c for c in txt)



    # vowels = "aiueoAIUEO"
    # res = []
    #
    # if num < 0 or type(num) == float:
    #     return 'invalid'
    #
    # for i in txt:
    #     if i in vowels:
    #         i = i * (num + 1)
    #         res.append(i)
    #     else:
    #         res.append(i)
    # return ''.join(res)

print(extend_vowels("Hello", 5))
print(extend_vowels("Edabit", 3))
print(extend_vowels("Extend", 0))
print(extend_vowels("A", 10))
print(extend_vowels("Vowel", 0.5))
print(extend_vowels("Nice", -8))

