"""
Powerful Prime Factor
Create a function that takes a positive integer and returns a string expressing how the number can be made by multiplying powers of its prime factors.

Examples
express_factors(2) ➞ "2"

express_factors(4) ➞ "2^2"

express_factors(10) ➞ "2 x 5"

express_factors(60) ➞ "2^2 x 3 x 5"
Notes
All inputs will be positive integers in the range 1 < n < 10,000.
If a factor is repeated express it in the form "x^y" where x is the factor and y is the number of repetitions of the factor.
If n is a prime number, return n as a string as in example #1 above.
Factors should appear in ascending order in the expression.
Make sure you include the space either side of the multiplication sign, " x ".
Check the Resources if you need to understand Prime Factorization.
"""

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def express_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        if n % divisor == 0:
            count = 0

            while n % divisor == 0:
                n //= divisor
                count += 1
            factors.append((divisor, count))
        divisor += 1

    result = ""

    for factor in factors:
        if isinstance(factor, int):
            result += str(factor)
        else:
            if factor[1] == 1:
                result += "{}".format(factor[0])
            else:
                result += "{}^{}".format(factor[0],factor[1])

            result += " × " if factor != factor[-1] else ""

    return result


print(express_factors(10))
print(express_factors(60)) # ➞ "2^2 x 3 x 5"
print(express_factors(323))
print(express_factors(5040))