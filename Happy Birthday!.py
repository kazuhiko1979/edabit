"""
Mubashir is getting old but he wants to celebrate his 20th or 21st birthday only. It is possible with some basic maths skills. He just needs to select the correct number base with your help!

For example, if his current age is 22, that's exactly 20 - in base 11. Similarly, 65 is exactly 21 - in base 32 and so on.

Create a function that takes his current age and returns the given age 20 (or 21) years, with number base in the format specified in the below examples.

Examples
happy_birthday(22) ➞ "Mubashir is just 20, in base 11!"
happy_birthday(65) ➞ "Mubashir is just 21, in base 32!"
happy_birthday(83) ➞ "Mubashir is just 21, in base 41!"
"""
def happy_birthday(age):
    age_20 = 20
    age_21 = 21
    base = age // 2
    if age % 2 == 0:
        return "Mubashir is just {}, in base {}!".format(age_20, base)
    else:
        return "Mubashir is just {}, in base {}!".format(age_21, base)

print(happy_birthday(22))
print(happy_birthday(65))
print(happy_birthday(83))
print(happy_birthday(32))
