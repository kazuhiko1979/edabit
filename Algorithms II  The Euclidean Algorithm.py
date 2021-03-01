"""
Algorithm
For the sake of simplicity I'll refer to the first number as "a", the second number as "b", and the remainder as "r". The algorithm can be broken down into four steps:

Ensure that "a" >= "b". If "a" < "b", swap them.
Find the remainder. Divide "a" by "b" and set "r" as the remainder.
Is "r" zero? If so terminate the function and return "b" (the second number).
Set "a" = "b" and "b" = "r" and start the algorithm over again.
Instructions
Create a recursive function that returns the GCD between two positive numbers using the Euclidean Algorithm.

Examples
euclidean(8, 6) ➞ 2
euclidean(25, 5) ➞ 5
euclidean(49, 14) ➞ 7

(問題) 1071 と 1029 の最大公約数を求める。
1071 を 1029 で割った余りは 42
1029 を 42 で割った余りは 21
42 を 21 で割った余りは 0
よって、最大公約数は21である。
"""
def euclidean(a, b):

    if b == 0:
        return a
    else:
        return euclidean(b, a%b)

print(euclidean(8, 6))
print(euclidean(25, 5))
print(euclidean(49, 14))