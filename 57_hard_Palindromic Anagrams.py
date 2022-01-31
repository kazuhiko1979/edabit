"""
Palindromic Anagrams
Given a word, create a function which returns whether or not it's possible to create a palindrome by rearranging the letters in the word.

Examples
is_palindrome_possible("rearcac") ➞ True
# You can make "racecar"

is_palindrome_possible("suhbeusheff") ➞ True
# You can make "sfuehbheufs" (not a real word but still a palindrome)

is_palindrome_possible("palindrome") ➞ False
# It's impossible
Notes
Trivially, words which are already palindromes return True.
Words are given in all lowercase.
"""

from collections import Counter

def is_palindrome_possible(str):

    freqs = {i:str.count(i) % 2 for i in str}
    # print(freqs)
    return list(freqs.values()).count(1) <= 1

    # return sum(str.count(i) % 2 for i in set(str)) <= 1

    # string = list(str)
    #
    # for i in range(len(str)):
    #     """ if the string has even element count """
    #     if len(str) % 2 == 0 and len(str) / 2 == len(set(str)):
    #         return True
    #     """ if the string has odd element count """
    #     if len(str) - ((len(str)-1)/2) == len(set(str)):
    #         return True
    # return False


    string = list(str)
    n = len(string)
    s_set = set(string)

    # print(string)
    dic = {}
    for i in string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    # print(dic)

    # dic = Counter(string)


    k = 0

    for char in s_set:
        # print(dic.get(char))
        if dic.get(char) % 2 != 0:
            k += 1

    if k > 1:
        return False
    else:
        return True

print(is_palindrome_possible("rearcac"))




