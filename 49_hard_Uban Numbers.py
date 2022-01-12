"""
Uban Numbers
A number n is called uban if its name (in English) does not contain the letter "u". In particular, it cannot contain the terms "four", "hundred", and "thousand", so the uban number following 99 is 1,000,000.

Write a function to determine if the given integer is uban.

Examples
is_uban(456) ➞ False

is_uban(25) ➞ True

is_uban(1098) ➞ False
"""

def is_uban(num):

    n = str(num)
    if '4' in n:
        if n.rindex('4') in [1, 4]:
            return False
    elif len(n) in [3,4,6]:
        return False
    return True


    # s = str(num)
    # print(s[-1])
    # return (len(s)<3 or len(s)>6) and s[-1] != '4'


    # if num == 40:
    #     return True
    # if len(str(num)) == 3 or len(str(num)) == 4 or '4' in str(num):
    #     return False
    # else:
    #     return True

print(is_uban(0))
print(is_uban(24))
print(is_uban(223))
print(is_uban(2051))
print(is_uban(627))
print(is_uban(6258))
print(is_uban(12))
print(is_uban(202))
print(is_uban(98))
print(is_uban(6592))
print(is_uban(393))
print(is_uban(10000096))
print(is_uban(40))
