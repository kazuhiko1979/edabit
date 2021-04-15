"""
A Fibonacci string is a precedence of the Fibonacci series. It works with any two characters of the English alphabet (as opposed to the numbers 0 and 1 in the Fibonacci series) as the initial items and concatenates them together as it progresses in a similar fashion as the Fibonacci series.

Examples
fib_str(3, ["j", "h"]) ➞ "j, h, hj"

fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"

fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"
"""

def fib_str(n, txt):

    res = []
    a, b = txt[0], txt[1]
    while n > 2:
        a, b, n = b, b+a, n-1
        res.append(b)
    res.insert(0, txt[0])
    res.insert(1, txt[1])
    return ', '.join(res)

    # fib = [1, 1]
    # if n == 1:
    #     fib = [1]
    # else:
    #     for k in range(2, n):
    #         fib.append(fib[k-1]+fib[k-2])
    # return fib

"""
[1, 1, 2]
[1, 1, 2, 3, 5]
[1, 1, 2, 3, 5, 8]
"""

print(fib_str(3, ["j", "h"]))
print(fib_str(5, ["e", "a"]))
print(fib_str(6, ["n", "k"]))
