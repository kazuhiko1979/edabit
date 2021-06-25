"""
Write a function that groups a string into parentheses cluster. Each cluster should be balanced.

Examples
split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
Notes
All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) in the same clust
"""


def split(txt):

    results = []
    p = ""

    for i in txt:
        p += i
        if p.count("(") == p.count(")"):
            results.append(p)
            p = ""

    return results

print(split(split("()()()")))
print(split("((()))"))

