"""
Meme Sum :)
For this challenge, forget how to add two numbers together. The best explanation on what to do for this function is this meme:

Alternative Text

Examples
meme_sum(26, 39) ➞ 515
# 2+3 = 5, 6+9 = 15
# 26 + 39 = 515

meme_sum(122, 81) ➞ 1103
# 1+0 = 1, 2+8 = 10, 2+1 = 3
# 122 + 81 = 1103

meme_sum(1222, 30277) ➞ 31499
"""

def meme_sum(a, b):

    # a, b = sorted([str(a), str(b)], key=len)
    #
    # res = ''
    # for i, j in zip(a.zfill(len(b)), b):
    #     res += str(int(i) + int(j))
    # return int(res)


    a = list(str(a))
    b = list(str(b))

    max_len = max(len(a), len(b))
    a = ['0'] * (max_len - len(a)) + a

    return int(''.join(str(int(a) + int(b)) for a, b in zip(a, b)))


    # result = []
    # putZeroCount = abs(len(str(a)) - len(str(b)))
    #
    # if len(str(a)) >= len(str(b)):
    #     b = str("0" * putZeroCount) + str(b)
    #
    #     for i in range(0, len(str(a))):
    #         result.append(str(int(str(a)[i]) + int(str(b)[i])))
    #     return int(''.join(result))
    #
    # else:
    #     a = str("0" * putZeroCount) + str(a)
    #
    #     for i in range(0, len(str(b))):
    #         result.append(str(int(str(a)[i]) + int(str(b)[i])))
    #     return int(''.join(result))


print(meme_sum(26, 39))
print(meme_sum(122, 81))
print(meme_sum(1222, 30277))