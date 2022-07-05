"""
Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for "." and "*" .

Examples
is_match("aa", "a") ➞ false
# "a" does not match the entire string "aa".

is_match("aa", "a*") ➞ true
# "*" means zero or more of the preceding element, "a".
# Therefore, by repeating "a" once, it becomes "aa".

is_match("ab", ".*") ➞ true
# ".*" means "zero or more (*) of any character (.)".
Notes
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""
import re

def is_match(s, p):


    # v2
    # if not re.search(r"[\.\*]", p):
    #     if s != p:
    #         return False
    # if re.match(p, s):
    #     return True
    # else:
    #     False

    # v1
    if s == p == "":
        return True
    if p == "":
        return False
    if p[-1] != "*":
        return is_match(s[:-1], p[:-1])
    if p[-2] == ".":
        return True
    r = s.index(p[-2])
    return is_match(s[:r], p[:-2])



print(is_match("aa", "a"))
print(is_match("aa", "a*"))
print(is_match("ab", ".*"))


