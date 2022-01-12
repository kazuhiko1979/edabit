"""
Possible Palindrome
Create a function that determines whether it is possible to build a palindrome from the characters in a string.

Examples
possible_palindrome("acabbaa") ➞ True
# Can make the following palindrome: "aabcbaa"

possible_palindrome("aacbdbc") ➞ True
# Can make the following palindrome: "abcdcba"

possible_palindrome("aacbdb") ➞ False

possible_palindrome("abacbb") ➞ False
"""

def possible_palindrome(txt):



    # res = {}
    #
    # for i in txt:
    #     if i not in res.keys():
    #         res[i] = 1
    #     else:
    #         res[i] += 1
    #
    # # 奇数リスト
    # oddList = []
    # # 偶数リスト
    # evenList = []
    #
    # for x in res.values():
    #     if x % 2 == 0:
    #         evenList.append(x)
    #     else:
    #         oddList.append(x)
    #
    # if len(oddList) == 1:
    #     return True
    # if not oddList and evenList:
    #     return True
    # else:
    #     return False


print(possible_palindrome("acabbaa"))
print(possible_palindrome("aacbdbc"))
print(possible_palindrome("aacbdb"))
print(possible_palindrome("abacbb"))
print(possible_palindrome("abb"))
print(possible_palindrome("bbb"))
print(possible_palindrome("bbaa"))
print(possible_palindrome("bbaacc"))
print(possible_palindrome("bbaaccd"))
print(possible_palindrome("bbaacd"))
print(possible_palindrome("abc"))
print(possible_palindrome("ab"))
print(possible_palindrome("aabbccddef"))

